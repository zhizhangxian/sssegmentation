## Introduction

<a href="https://github.com/facebookresearch/detectron2/tree/master/projects/PointRend">Official Repo</a>

<a href="https://github.com/SegmentationBLWX/sssegmentation/blob/main/ssseg/modules/models/segmentors/pointrend/pointrend.py">Code Snippet</a>

<details>
<summary align="left"><a href="https://arxiv.org/pdf/1912.08193.pdf">PointRend (CVPR'2020)</a></summary>

```latex
@inproceedings{kirillov2020pointrend,
    title={Pointrend: Image segmentation as rendering},
    author={Kirillov, Alexander and Wu, Yuxin and He, Kaiming and Girshick, Ross},
    booktitle={Proceedings of the IEEE/CVF conference on computer vision and pattern recognition},
    pages={9799--9808},
    year={2020}
}
```

</details>


## Results

#### PASCAL VOC

| Backbone  | Pretrain               | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                                                                                                                                                                                                                                                                                                                                                                                             |
| :-:       | :-:                    | :-:        | :-:                                  | :-:             | :-:    | :-:                                                                                                                                                                                                                                                                                                                                                                                                  |
| R-50-D32  | ImageNet-1k-224x224    | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 69.84% | [cfg](https://raw.githubusercontent.com/SegmentationBLWX/sssegmentation/main/ssseg/configs/pointrend/pointrend_resnet50os32_voc.py) &#124; [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_pointrend/pointrend_resnet50os32_voc.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_pointrend/pointrend_resnet50os32_voc.log)    |
| R-101-D32 | ImageNet-1k-224x224    | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 72.31% | [cfg](https://raw.githubusercontent.com/SegmentationBLWX/sssegmentation/main/ssseg/configs/pointrend/pointrend_resnet101os32_voc.py) &#124; [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_pointrend/pointrend_resnet101os32_voc.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_pointrend/pointrend_resnet101os32_voc.log) |

#### ADE20k

| Backbone  | Pretrain               | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                                                                                                                                                                                                                                                                                                                                                                                                      |
| :-:       | :-:                    | :-:        | :-:                                  | :-:             | :-:    | :-:                                                                                                                                                                                                                                                                                                                                                                                                           |
| R-50-D32  | ImageNet-1k-224x224    | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 37.80% | [cfg](https://raw.githubusercontent.com/SegmentationBLWX/sssegmentation/main/ssseg/configs/pointrend/pointrend_resnet50os32_ade20k.py) &#124; [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_pointrend/pointrend_resnet50os32_ade20k.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_pointrend/pointrend_resnet50os32_ade20k.log)    |
| R-101-D32 | ImageNet-1k-224x224    | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 40.26% | [cfg](https://raw.githubusercontent.com/SegmentationBLWX/sssegmentation/main/ssseg/configs/pointrend/pointrend_resnet101os32_ade20k.py) &#124; [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_pointrend/pointrend_resnet101os32_ade20k.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_pointrend/pointrend_resnet101os32_ade20k.log) |

#### CityScapes

| Backbone  | Pretrain               | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :-:       | :-:                    | :-:        | :-:                                  | :-:             | :-:    | :-:                                                                                                                                                                                                                                                                                                                                                                                                                       |
| R-50-D32  | ImageNet-1k-224x224    | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 76.89% | [cfg](https://raw.githubusercontent.com/SegmentationBLWX/sssegmentation/main/ssseg/configs/pointrend/pointrend_resnet50os32_cityscapes.py) &#124; [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_pointrend/pointrend_resnet50os32_cityscapes.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_pointrend/pointrend_resnet50os32_cityscapes.log)    |
| R-101-D32 | ImageNet-1k-224x224    | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 78.80% | [cfg](https://raw.githubusercontent.com/SegmentationBLWX/sssegmentation/main/ssseg/configs/pointrend/pointrend_resnet101os32_cityscapes.py) &#124; [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_pointrend/pointrend_resnet101os32_cityscapes.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_pointrend/pointrend_resnet101os32_cityscapes.log) |


## More

You can also download the model weights from following sources:

- BaiduNetdisk: https://pan.baidu.com/s/1gD-NJJWOtaHCtB0qHE79rA with access code **s757**