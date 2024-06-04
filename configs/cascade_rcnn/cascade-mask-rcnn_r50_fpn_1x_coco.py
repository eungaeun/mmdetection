_base_ = [
    '../_base_/models/cascade-mask-rcnn_r50_fpn.py',
    # '../_base_/datasets/coco_instance.py',
    '../_base_/datasets/coco_detection_pe_module.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]
