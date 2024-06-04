_base_ = '..\..\configs\swin\mask-rcnn_swin-t-p4-w7_fpn_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict( type='Shared2FCBBoxHead', num_classes=7, _delete_=True)))
metrics = ['bbox']
# Modify dataset related settings
data_root = '../data/pe_module/'
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
load_from = 'https://download.openmmlab.com/mmdetection/v2.0/swin/mask_rcnn_swin-t-p4-w7_fpn_1x_coco/mask_rcnn_swin-t-p4-w7_fpn_1x_coco_20210902_120937-9d6b7cfa.pth'
