# YOLOv5 Config


yolov5_cfg = {
    'yolov5_n':{
        # ---------------- Model config ----------------
        ## Backbone
        'backbone': 'cspdarknet',
        'bk_act': 'silu',
        'bk_norm': 'BN',
        'bk_dpw': False,
        'width': 0.15, #best:0.25
        'depth': 0.24, #best:0.34
        'stride': [8, 16, 32],  # P3, P4, P5
        'max_stride': 32,
        ## FPN
        'fpn': 'yolov5_pafpn',
        'fpn_reduce_layer': 'Conv',
        'fpn_downsample_layer': 'Conv',
        'fpn_core_block': 'CSPBlock',
        'fpn_act': 'silu',
        'fpn_norm': 'BN',
        'fpn_depthwise': False,
        ## Head
        'head': 'decoupled_head',
        'head_act': 'silu',
        'head_norm': 'BN',
        'num_cls_head': 2,
        'num_reg_head': 2,
        'head_depthwise': False,
        'anchor_size': [[10, 13],   [16, 30],   [33, 23],     # P3
                        [30, 61],   [62, 45],   [59, 119],    # P4
                        [116, 90],  [156, 198], [373, 326]],  # P5
        # ---------------- Data process config ----------------
        ## input
        'multi_scale': [0.5, 1.25],   # 320 -> 800
        'trans_type': 'yolo_n',
        # ---------------- Assignment config ----------------
        ## matcher
        'anchor_thresh': 4.0,
        # ---------------- Loss config ----------------
        ## loss weight
        'loss_obj_weight': 1.0,
        'loss_cls_weight': 1.0,
        'loss_box_weight': 5.0,
        # ---------------- Train config ----------------
        'trainer_type': 'yolo',
    },

    'yolov5_s':{
        # ---------------- Model config ----------------
        ## Backbone
        'backbone': 'cspdarknet',
        'bk_act': 'silu',
        'bk_norm': 'BN',
        'bk_dpw': False,
        'width': 0.50,
        'depth': 0.34,
        'stride': [8, 16, 32],  # P3, P4, P5
        'max_stride': 32,
        ## FPN
        'fpn': 'yolov5_pafpn',
        'fpn_reduce_layer': 'Conv',
        'fpn_downsample_layer': 'Conv',
        'fpn_core_block': 'CSPBlock',
        'fpn_act': 'silu',
        'fpn_norm': 'BN',
        'fpn_depthwise': False,
        ## Head
        'head': 'decoupled_head',
        'head_act': 'silu',
        'head_norm': 'BN',
        'num_cls_head': 2,
        'num_reg_head': 2,
        'head_depthwise': False,
        'anchor_size': [[10, 13],   [16, 30],   [33, 23],     # P3
                        [30, 61],   [62, 45],   [59, 119],    # P4
                        [116, 90],  [156, 198], [373, 326]],  # P5
        # ---------------- Data process config ----------------
        ## input
        'multi_scale': [0.5, 1.25],   # 320 -> 800
        'trans_type': 'yolo_s',
        # ---------------- Assignment config ----------------
        ## matcher
        'anchor_thresh': 4.0,
        # ---------------- Loss config ----------------
        ## loss weight
        'loss_obj_weight': 1.0,
        'loss_cls_weight': 1.0,
        'loss_box_weight': 5.0,
        # ---------------- Train config ----------------
        'trainer_type': 'yolo',
    },

    'yolov5_m':{
        # ---------------- Model config ----------------
        ## Backbone
        'backbone': 'cspdarknet',
        'bk_act': 'silu',
        'bk_norm': 'BN',
        'bk_dpw': False,
        'width': 0.75,
        'depth': 0.67,
        'stride': [8, 16, 32],  # P3, P4, P5
        'max_stride': 32,
        ## FPN
        'fpn': 'yolov5_pafpn',
        'fpn_reduce_layer': 'Conv',
        'fpn_downsample_layer': 'Conv',
        'fpn_core_block': 'CSPBlock',
        'fpn_act': 'silu',
        'fpn_norm': 'BN',
        'fpn_depthwise': False,
        ## Head
        'head': 'decoupled_head',
        'head_act': 'silu',
        'head_norm': 'BN',
        'num_cls_head': 2,
        'num_reg_head': 2,
        'head_depthwise': False,
        'anchor_size': [[10, 13],   [16, 30],   [33, 23],     # P3
                        [30, 61],   [62, 45],   [59, 119],    # P4
                        [116, 90],  [156, 198], [373, 326]],  # P5
        # ---------------- Data process config ----------------
        ## input
        'multi_scale': [0.5, 1.25],   # 320 -> 800
        'trans_type': 'yolo_m',
        # ---------------- Assignment config ----------------
        ## matcher
        'anchor_thresh': 4.0,
        # ---------------- Loss config ----------------
        ## loss weight
        'loss_obj_weight': 1.0,
        'loss_cls_weight': 1.0,
        'loss_box_weight': 5.0,
        # ---------------- Train config ----------------
        'trainer_type': 'yolo',
    },

    'yolov5_l':{
        # ---------------- Model config ----------------
        ## Backbone
        'backbone': 'cspdarknet',
        'bk_act': 'silu',
        'bk_norm': 'BN',
        'bk_dpw': False,
        'width': 1.0,
        'depth': 1.0,
        'stride': [8, 16, 32],  # P3, P4, P5
        'max_stride': 32,
        ## FPN
        'fpn': 'yolov5_pafpn',
        'fpn_reduce_layer': 'Conv',
        'fpn_downsample_layer': 'Conv',
        'fpn_core_block': 'CSPBlock',
        'fpn_act': 'silu',
        'fpn_norm': 'BN',
        'fpn_depthwise': False,
        ## Head
        'head': 'decoupled_head',
        'head_act': 'silu',
        'head_norm': 'BN',
        'num_cls_head': 2,
        'num_reg_head': 2,
        'head_depthwise': False,
        'anchor_size': [[10, 13],   [16, 30],   [33, 23],     # P3
                        [30, 61],   [62, 45],   [59, 119],    # P4
                        [116, 90],  [156, 198], [373, 326]],  # P5
        # ---------------- Data process config ----------------
        ## input
        'multi_scale': [0.5, 1.25],   # 320 -> 800
        'trans_type': 'yolo_l',
        # ---------------- Assignment config ----------------
        ## matcher
        'anchor_thresh': 4.0,
        # ---------------- Loss config ----------------
        ## loss weight
        'loss_obj_weight': 1.0,
        'loss_cls_weight': 1.0,
        'loss_box_weight': 5.0,
        # ---------------- Train config ----------------
        'trainer_type': 'yolo',
    },

    'yolov5_x':{
        # ---------------- Model config ----------------
        ## Backbone
        'backbone': 'cspdarknet',
        'bk_act': 'silu',
        'bk_norm': 'BN',
        'bk_dpw': False,
        'width': 1.25,
        'depth': 1.34,
        'stride': [8, 16, 32],  # P3, P4, P5
        'max_stride': 32,
        ## FPN
        'fpn': 'yolov5_pafpn',
        'fpn_reduce_layer': 'Conv',
        'fpn_downsample_layer': 'Conv',
        'fpn_core_block': 'CSPBlock',
        'fpn_act': 'silu',
        'fpn_norm': 'BN',
        'fpn_depthwise': False,
        ## Head
        'head': 'decoupled_head',
        'head_act': 'silu',
        'head_norm': 'BN',
        'num_cls_head': 2,
        'num_reg_head': 2,
        'head_depthwise': False,
        'anchor_size': [[10, 13],   [16, 30],   [33, 23],     # P3
                        [30, 61],   [62, 45],   [59, 119],    # P4
                        [116, 90],  [156, 198], [373, 326]],  # P5
        # ---------------- Data process config ----------------
        ## input
        'multi_scale': [0.5, 1.25],   # 320 -> 800
        'trans_type': 'yolo_x',
        # ---------------- Assignment config ----------------
        ## matcher
        'anchor_thresh': 4.0,
        # ---------------- Loss config ----------------
        ## loss weight
        'loss_obj_weight': 1.0,
        'loss_cls_weight': 1.0,
        'loss_box_weight': 5.0,
        # ---------------- Train config ----------------
        'trainer_type': 'yolo',
    },
}
