# the new config inherits the base configs to highlight the necessary modification
# _base_ = '/workspace/mmdetection/configs/cascade_rcnn/cascade-mask-rcnn_r50_fpn_1x_coco.py'
_base_ ='/workspace/mmdetection/configs/faster_rcnn/faster-rcnn_r50_fpn_1x_pe_module.py'



# 1. dataset settings
dataset_type = 'Pe_Dataset'
classes = ('blue_s', 'blue_m', 'blue_l', 'black_m', 'black_s', 'white_l', 'module')
# data_root='/workspace/mmdetection/data/pe_module_24_1_26'

backend_args = None
file_client_args = None
# train_dataloader = dict(
#     batch_size=8,
#     num_workers=4,
#     dataset=dict(
#         type=dataset_type,
#         # explicitly add your class names to the field `metainfo`
#         # metainfo=dict(classes=classes),
#         # classes=classes,
#         data_root=data_root,
#         ann_file=data_root+'/train/PE_train_coco.json',
#         data_prefix=dict(img='train')
#         )
#     )

# val_dataloader = dict(
#     batch_size=8,
#     num_workers=4,
#     dataset=dict(
#         type=dataset_type,
#         test_mode=True,
#         # explicitly add your class names to the field `metainfo`
#         # metainfo=dict(classes=classes),
#         # classes=classes,
#         data_root=data_root,
#         ann_file=data_root+'/val/PE_val_coco.json',
#         data_prefix=dict(img='val')
#         )
#     )

# test_dataloader = dict(
#     batch_size=8,
#     num_workers=4,
#     dataset=dict(
#         type=dataset_type,
#         test_mode=True,
#         # explicitly add your class names to the field `metainfo`
#         # metainfo=dict(classes=classes),
#         # classes=classes,
#         data_root=data_root,
#         ann_file=data_root+'/test/PE_test_coco.json',
#         data_prefix=dict(img='test')
#         )
#     )

# 2. model settings

# explicitly over-write all the `num_classes` field from default 80 to 5.
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
#     # mask_head=dict(num_classes=7)
#     # mask_head=None
#     ))

# model = dict(
#     roi_head=dict(
#         bbox_head=dict(num_classes=7),
#         mask_head=dict(num_classes=7)))

# metrics = ['bbox']