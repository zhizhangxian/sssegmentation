'''vocaug_mobilevit_512x512'''
import os


'''DATASET_CFG_VOCAUG_MOBILEVIT_512x512'''
DATASET_CFG_VOCAUG_MOBILEVIT_512x512 = {
    'type': 'VOCDataset',
    'rootdir': os.path.join(os.getcwd(), 'VOCdevkit/VOC2012'),
    'train': {
        'set': 'trainaug',
        'data_pipelines': [
            ('RandomChoiceResize', {'scales': [int(512 * x * 0.1) for x in range(5, 21)], 'resize_type': 'ResizeShortestEdge', 'max_size': 2048}),
            ('RandomCrop', {'crop_size': (512, 512), 'one_category_max_ratio': 0.75}),
            ('RandomFlip', {'flip_prob': 0.5}),
            ('RandomRotation', {'angle_upper': 10, 'rotation_prob': 0.5}),
            ('RandomGaussianBlur', {'prob': 0.5}),
            ('PhotoMetricDistortion', {}),
            ('Normalize', {'mean': [123.675, 116.28, 103.53], 'std': [58.395, 57.12, 57.375]}),
            ('ToTensor', {}),
            ('Padding', {'output_size': (512, 512), 'data_type': 'tensor'}),
        ],
    },
    'test': {
        'set': 'val',
        'data_pipelines': [
            ('Resize', {'output_size': (2048, 512), 'keep_ratio': True, 'scale_range': None}),
            ('Normalize', {'mean': [123.675, 116.28, 103.53], 'std': [58.395, 57.12, 57.375]}),
            ('ToTensor', {}),
        ],
    }
}