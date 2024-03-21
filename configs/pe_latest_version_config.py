
# # the new config inherits the base configs to highlight the necessary modification
# _base_ = 'cascade_rcnn/cascade-mask-rcnn_r50_fpn_1x_coco.py'

# # /workspace/mmdetection/configs/cascade_rcnn
# # 1. dataset settings
# dataset_type = 'CocoDataset'
# # dataset_type = 'Pe_Dataset'
# classes = ('blue_s', 'blue_m', 'blue_l', 'black_m', 'black_s', 'white_l', 'module')
# data = dict(
#     samples_per_gpu=2,
#     workers_per_gpu=2,
#     train=dict(
#         type=dataset_type,
#         # explicitly add your class names to the field `classes`
#         classes=classes,
#         ann_file='data/pe_module_24_1_26/annotations/PE_train_coco.json',
#         img_prefix='data/pe_module_24_1_26/train/'),
#     val=dict(
#         type=dataset_type,
#         # explicitly add your class names to the field `classes`
#         classes=classes,
#         ann_file='/workspace/mmdetection/data/pe_module_24_1_26/annotations/PE_val_coco.json',
#         img_prefix='/workspace/mmdetection/data/pe_module_24_1_26/val/'),
#     test=dict(
#         type=dataset_type,
#         # explicitly add your class names to the field `classes`
#         classes=classes,
#         ann_file='/workspace/mmdetection/data/pe_module_24_1_26/annotations/PE_test_coco.json',
#         img_prefix='/workspace/mmdetection/data/pe_module_24_1_26/test/'))

# # 2. model settings

# # explicitly over-write all the `num_classes` field from default 80 to 5.
# model = dict(
#     roi_head=dict(
#         bbox_head=[
#             dict(
#                 type='Shared2FCBBoxHead',
#                 # explicitly over-write all the `num_classes` field from default 80 to 5.
#                 num_classes=7),
#             dict(
#                 type='Shared2FCBBoxHead',
#                 # explicitly over-write all the `num_classes` field from default 80 to 5.
#                 num_classes=7),
#             dict(
#                 type='Shared2FCBBoxHead',
#                 # explicitly over-write all the `num_classes` field from default 80 to 5.
#                 num_classes=7)],
#     # explicitly over-write all the `num_classes` field from default 80 to 5.
#     mask_head=dict(num_classes=7)))



_base_ = 'cascade_rcnn/cascade-mask-rcnn_r50_fpn_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict( type='Shared2FCBBoxHead', num_classes=7, _delete_=True)))
metrics = ['bbox']
# Modify dataset related settings
data_root = 'data/pe_module_24_1_26/'
metainfo = {
    'classes': ('blue_s', 'blue_m', 'blue_l', 'black_m', 'black_s', 'white_l', 'module'),
    'palette': [
        (220, 20, 60),(120, 220, 40),(22, 210, 80),(100, 250, 150),
        (120, 70, 200),(60, 20, 220),(150, 200, 160)
    ]
}
train_dataloader = dict(
    batch_size=1,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='annotations/PE_train_coco.json',
        data_prefix=dict(img='train/')))
val_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='annotations/PE_val_coco.json',
        data_prefix=dict(img='val/')))
test_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='annotations/PE_test_coco.json',
        data_prefix=dict(img='test/')))

# Modify metric related settings
val_evaluator = dict(ann_file=data_root + 'annotations/PE_val_coco.json')
test_evaluator = dict(ann_file=data_root + 'annotations/PE_test_coco.json')

# We can use the pre-trained Mask RCNN model to obtain higher performance
# load_from = 'https://download.openmmlab.com/mmdetection/v2.0/mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'