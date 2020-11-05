# Deeplabv3Plus
```
@inproceedings{chen2018encoder,
  title={Encoder-decoder with atrous separable convolution for semantic image segmentation},
  author={Chen, Liang-Chieh and Zhu, Yukun and Papandreou, George and Schroff, Florian and Adam, Hartwig},
  booktitle={Proceedings of the European conference on computer vision (ECCV)},
  pages={801--818},
  year={2018}
}
The implemented details see https://arxiv.org/pdf/1802.02611.pdf.
```


# Results

## PASCAL VOC
| Backbone                        | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | FPS    |
| :-:                             | :-:        | :-:                                  | :-:             | :-:    | :-:    |
| ResNet50 (OS=8, PRE=ImageNet)   | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 77.66% | -      |
| ResNet50 (OS=16, PRE=ImageNet)  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 76.68% | -      |
| ResNet101 (OS=8, PRE=ImageNet)  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 79.85% | -      |
| ResNet101 (OS=16, PRE=ImageNet) | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 79.09% | -      |

## ADE20k
| Backbone                        | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | FPS    |
| :-:                             | :-:        | :-:                                  | :-:             | :-:    | :-:    |
| ResNet50 (OS=8, PRE=ImageNet)   | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 43.22% | -      |
| ResNet50 (OS=16, PRE=ImageNet)  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 42.30% | -      |
| ResNet101 (OS=8, PRE=ImageNet)  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 45.64% | -      |
| ResNet101 (OS=16, PRE=ImageNet) | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 43.51% | -      |

## CityScapes
| Backbone                        | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | FPS    |
| :-:                             | :-:        | :-:                                  | :-:             | :-:    | :-:    |
| ResNet50 (OS=8, PRE=ImageNet)   | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | -      | -      |
| ResNet50 (OS=16, PRE=ImageNet)  | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | -      | -      |
| ResNet101 (OS=8, PRE=ImageNet)  | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | -      | -      |
| ResNet101 (OS=16, PRE=ImageNet) | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | -      | -      |