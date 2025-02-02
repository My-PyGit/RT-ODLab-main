import argparse
import os

from copy import deepcopy
import torch

from evaluator.voc_evaluator import VOCAPIEvaluator
from evaluator.coco_evaluator import COCOAPIEvaluator
from evaluator.crowdhuman_evaluator  import CrowdHumanEvaluator
from evaluator.widerface_evaluator import WiderFaceEvaluator
from evaluator.customed_evaluator import CustomedEvaluator

# load transform
from dataset.build import build_transform

# load some utils
from utils.misc import load_weight
from utils.misc import compute_flops

from config import build_dataset_config, build_model_config, build_trans_config
from models.detectors import build_model


def parse_args():
    parser = argparse.ArgumentParser(description='Real-time Object Detection LAB')
    # Basic setting
    parser.add_argument('-size', '--img_size', default=640, type=int,
                        help='the max size of input image')
    parser.add_argument('--cuda', action='store_true', default=False,
                        help='Use cuda')

    # Model setting
    parser.add_argument('-m', '--model', default='yolov5_n', type=str,
                        help='build yolo')
    parser.add_argument('--weight', default='weights/voc/yolov5_n/yolov5_n_best_tiny_150epoch.pth',
                        type=str, help='Trained state_dict file path to open')
    parser.add_argument('-ct', '--conf_thresh', default=0.001, type=float,
                        help='confidence threshold')
    parser.add_argument('-nt', '--nms_thresh', default=0.7, type=float,
                        help='NMS threshold')
    parser.add_argument('--topk', default=1000, type=int,
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
    parser.add_argument('--mosaic', default=None, type=float,
                        help='mosaic augmentation.')
    parser.add_argument('--mixup', default=None, type=float,
                        help='mixup augmentation.')
    parser.add_argument('--load_cache', action='store_true', default=False,
                        help='load data into memory.')

    # TTA
    parser.add_argument('-tta', '--test_aug', action='store_true', default=False,
                        help='use test augmentation.')

    return parser.parse_args()



def voc_test(model, data_dir, device, transform):
    evaluator = VOCAPIEvaluator(data_dir=data_dir,
                                device=device,
                                transform=transform,
                                display=True)

    # VOC evaluation
    evaluator.evaluate(model)


def coco_test(model, data_dir, device, transform, test=False):
    if test:
        # test-dev
        print('test on test-dev 2017')
        evaluator = COCOAPIEvaluator(
                        data_dir=data_dir,
                        device=device,
                        testset=True,
                        transform=transform)

    else:
        # eval
        evaluator = COCOAPIEvaluator(
                        data_dir=data_dir,
                        device=device,
                        testset=False,
                        transform=transform)

    # COCO evaluation
    evaluator.evaluate(model)


def crowdhuman_test(model, data_dir, device, transform):
    evaluator = CrowdHumanEvaluator(
        data_dir=data_dir,
        device=device,
        image_set='val',
        transform=transform)

    # WiderFace evaluation
    evaluator.evaluate(model)


def widerface_test(model, data_dir, device, transform):
    evaluator = WiderFaceEvaluator(
        data_dir=data_dir,
        device=device,
        image_set='val',
        transform=transform)

    # WiderFace evaluation
    evaluator.evaluate(model)


def customed_test(model, data_dir, device, transform):
    evaluator = CustomedEvaluator(
        data_dir=data_dir,
        device=device,
        image_set='val',
        transform=transform)

    # WiderFace evaluation
    evaluator.evaluate(model)


if __name__ == '__main__':
    args = parse_args()
    # cuda
    if args.cuda:
        print('use cuda')
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")

    # Dataset & Model Config
    data_cfg = build_dataset_config(args)
    model_cfg = build_model_config(args)
    trans_cfg = build_trans_config(model_cfg['trans_type'])
    
    data_dir = os.path.join(args.root, data_cfg['data_name'])
    num_classes = data_cfg['num_classes']

    # build model
    model = build_model(args, model_cfg, device, num_classes, False)

    # load trained weight
    model = load_weight(model, args.weight, args.fuse_conv_bn)
    model.to(device).eval()

    # compute FLOPs and Params
    model_copy = deepcopy(model)
    model_copy.trainable = False
    model_copy.eval()
    compute_flops(
        model=model_copy,
        img_size=args.img_size, 
        device=device)
    del model_copy

    # transform
    val_transform, trans_cfg = build_transform(args, trans_cfg, model_cfg['max_stride'], is_train=False)

    # evaluation
    with torch.no_grad():
        if args.dataset == 'voc':
            voc_test(model, data_dir, device, val_transform)
        elif args.dataset == 'coco-val' or args.dataset == 'coco':
            coco_test(model, data_dir, device, val_transform, test=False)
        elif args.dataset == 'coco-test':
            coco_test(model, data_dir, device, val_transform, test=True)
        elif args.dataset == 'ourdataset':
            customed_test(model, data_dir, device, val_transform)
