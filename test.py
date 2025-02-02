import argparse
import cv2
import os
import time
import numpy as np
from copy import deepcopy
import torch

# load transform
from dataset.build import build_dataset, build_transform

# load some utils
from utils.misc import load_weight, compute_flops
from utils.box_ops import rescale_bboxes
from utils.vis_tools import visualize

from config import build_dataset_config, build_model_config, build_trans_config
from models.detectors import build_model


def parse_args():
    parser = argparse.ArgumentParser(description='Real-time Object Detection LAB')
    # Basic setting
    parser.add_argument('-size', '--img_size', default=640, type=int,
                        help='the max size of input image')
    parser.add_argument('--show', action='store_true', default=True,
                        help='show the visulization results.')
    parser.add_argument('--save', action='store_true', default=False,
                        help='save the visulization results.')
    parser.add_argument('--cuda', action='store_true', default=False, 
                        help='use cuda.')
    parser.add_argument('--save_folder', default='det_results/', type=str,
                        help='Dir to save results')
    parser.add_argument('-ws', '--window_scale', default=1.0, type=float,
                        help='resize window of cv2 for visualization.')
    parser.add_argument('--resave', action='store_true', default=False, 
                        help='resave checkpoints without optimizer state dict.')

    # Model setting
    parser.add_argument('-m', '--model', default='yolov5_n', type=str,
                        help='build yolo')
    parser.add_argument('--weight', default='weights/voc/yolov5_n/yolov5_n_best_tiny_150epoch.pth',
                        type=str, help='Trained state_dict file path to open')
    parser.add_argument('-ct', '--conf_thresh', default=0.3, type=float,
                        help='confidence threshold')
    parser.add_argument('-nt', '--nms_thresh', default=0.5, type=float,
                        help='NMS threshold')
    parser.add_argument('--topk', default=100, type=int,
                        help='topk candidates dets of each level before NMS')
    parser.add_argument("--no_decode", action="store_true", default=False,
                        help="not decode in inference or yes")
    parser.add_argument('--fuse_conv_bn', action='store_true', default=False,
                        help='fuse Conv & BN')
    parser.add_argument('--no_multi_labels', action='store_true', default=False,
                        help='Perform post-process with multi-labels trick.')
    parser.add_argument('--nms_class_agnostic', action='store_true', default=False,
                        help='Perform NMS operations regardless of category.')

    # Data setting
    parser.add_argument('--root', default='F:/subject/Graduation_Project/dataset/',
                        help='data root')
    parser.add_argument('-d', '--dataset', default='voc',
                        help='coco, voc.')
    parser.add_argument('--min_box_size', default=8.0, type=float,
                        help='min size of target bounding box.')
    parser.add_argument('--mosaic', default=None, type=float,
                        help='mosaic augmentation.')
    parser.add_argument('--mixup', default=None, type=float,
                        help='mixup augmentation.')
    parser.add_argument('--load_cache', action='store_true', default=False,
                        help='load data into memory.')

    return parser.parse_args()


@torch.no_grad()
def test_det(args,
             model, 
             device, 
             dataset,
             transform=None,
             class_colors=None, 
             class_names=None, 
             class_indexs=None):
    num_images = len(dataset)
    save_path = os.path.join('det_results/', args.dataset, args.model)
    os.makedirs(save_path, exist_ok=True)

    for index in range(num_images):
        print('Testing image {:d}/{:d}....'.format(index+1, num_images))
        image, _ = dataset.pull_image(index) #每次读取一张图片，没有经过处理

        orig_h, orig_w, _ = image.shape

        # prepare
        x, _, ratio = transform(image)
        x = x.unsqueeze(0).to(device)

        t0 = time.time()
        # inference
        outputs = model(x)
        scores = outputs['scores']
        labels = outputs['labels']
        bboxes = outputs['bboxes']
        print("detection time used ", time.time() - t0, "s")
        
        # rescale bboxes重新调整边界框（bounding boxes）的尺寸
        bboxes = rescale_bboxes(bboxes, [orig_w, orig_h], ratio)

        # vis detection
        img_processed = visualize(image=image,
                                  bboxes=bboxes,
                                  scores=scores,
                                  labels=labels,
                                  class_colors=class_colors,
                                  class_names=class_names,
                                  class_indexs=class_indexs)
        if args.show:
            h, w = img_processed.shape[:2]
            sw, sh = int(w*args.window_scale), int(h*args.window_scale)
            cv2.namedWindow('detection', 0)
            cv2.resizeWindow('detection', sw, sh)
            cv2.imshow('detection', img_processed)
            cv2.waitKey(0)

        if args.save:
            # save result
            cv2.imwrite(os.path.join(save_path, str(index).zfill(6) +'.jpg'), img_processed)


if __name__ == '__main__':
    args = parse_args()
    # cuda
    if args.cuda:
        print('use cuda')
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")
        print('use cpu')

    # Dataset & Model Config
    data_cfg = build_dataset_config(args)
    model_cfg = build_model_config(args)
    trans_cfg = build_trans_config(model_cfg['trans_type'])

    # Transform
    val_transform, trans_cfg = build_transform(args, trans_cfg, model_cfg['max_stride'], is_train=False)

    # Dataset
    dataset, dataset_info = build_dataset(args, data_cfg, trans_cfg, val_transform, is_train=False)
    num_classes = dataset_info['num_classes']

    np.random.seed(0)
    class_colors = [(np.random.randint(255),
                     np.random.randint(255),
                     np.random.randint(255)) for _ in range(num_classes)]

    # build model
    model = build_model(args, model_cfg, device, num_classes, False)

    # load trained weight
    model = load_weight(model, args.weight, args.fuse_conv_bn)
    model.to(device).eval()

    # # compute FLOPs and Params
    # model_copy = deepcopy(model)
    # model_copy.trainable = False
    # model_copy.eval()
    # compute_flops(
    #     model=model_copy,
    #     img_size=args.img_size,
    #     device=device)
    # del model_copy
    #
    # # resave model weight
    # if args.resave:
    #     print('Resave: {}'.format(args.model.upper()))
    #     checkpoint = torch.load(args.weight, map_location='cpu')
    #     checkpoint_path = 'weights/{}/{}/{}_pure.pth'.format(args.dataset, args.model, args.model)
    #     torch.save({'model': model.state_dict(),
    #                 'mAP': checkpoint.pop("mAP"),
    #                 'epoch': checkpoint.pop("epoch")},
    #                 checkpoint_path)
    #
    # print("================= DETECT =================")
    # run
    test_det(args=args,
             model=model, 
             device=device, 
             dataset=dataset,
             transform=val_transform,
             class_colors=class_colors,
             class_names=dataset_info['class_names'],
             class_indexs=dataset_info['class_indexs'],
             )
