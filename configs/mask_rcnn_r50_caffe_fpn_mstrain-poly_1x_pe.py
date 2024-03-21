# The new config inherits a base config to highlight the necessary modification
_base_ = 'mask_rcnn/mask-rcnn_r50-caffe_fpn_ms-poly-1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=7),
        mask_head=dict(num_classes=7)))

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('blue_s', 'blue_m', 'blue_l', 'black_m', 'black_s', 'white_l', 'module')
data = dict(
    train=dict(
        img_prefix='pe_module_24_1_26/images/train',
        classes=classes,
        num_classes = 7,
        ann_file='pe_module_24_1_26/PE_test_coco.json'),
    val=dict(
        img_prefix='pe_module_24_1_26/images/val',
        classes=classes,
        num_classes = 7,
        ann_file='pe_module_24_1_26/PE_test_coco.json'),
    test=dict(
        img_prefix='pe_module_24_1_26/images/test',
        classes=classes,
        num_classes = 7,
        ann_file='pe_module_24_1_26/PE_test_coco.json'))

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'checkpoints/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'