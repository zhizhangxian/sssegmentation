'''
Function:
    color map for visualizing the segmentation mask
Author:
    Zhenchao Jin
'''
import os


'''define all'''
__all__ = ['BuildPalette']


'''lip palette'''
lip_palette = [(0, 0, 0), (127, 0, 0), (254, 0, 0), (0, 84, 0), (169, 0, 50), (254, 84, 0), (0, 0, 84),
               (0, 118, 220), (84, 84, 0), (0, 84, 84), (84, 50, 0), (51, 85, 127), (0, 127, 0), (0, 0, 254), 
               (50, 169, 220), (0, 254, 254), (84, 254, 169), (169, 254, 84), (254, 254, 0), (254, 169, 0)]


'''cihp palette'''
cihp_palette = [(0, 0, 0), (127, 0, 0), (254, 0, 0), (0, 84, 0), (169, 0, 50), (254, 84, 0), (0, 0, 84),
               (0, 118, 220), (84, 84, 0), (0, 84, 84), (84, 50, 0), (51, 85, 127), (0, 127, 0), (0, 0, 254), 
               (50, 169, 220), (0, 254, 254), (84, 254, 169), (169, 254, 84), (254, 254, 0), (254, 169, 0)]


'''voc context palette'''
voccontext_palette = [(0, 0, 0), (128, 0, 0), (0, 128, 0), (128, 128, 0), (0, 0, 128), (128, 0, 128),
                      (0, 128, 128), (128, 128, 128), (64, 0, 0), (192, 0, 0), (64, 128, 0), (192, 128, 0),
                      (64, 0, 128), (192, 0, 128), (64, 128, 128), (192, 128, 128), (0, 64, 0), (128, 64, 0),
                      (0, 192, 0), (128, 192, 0), (0, 64, 128), (128, 64, 128), (0, 192, 128), (128, 192, 128),
                      (64, 64, 0), (192, 64, 0), (64, 192, 0), (192, 192, 0), (64, 64, 128), (192, 64, 128),
                      (64, 192, 128), (192, 192, 128), (0, 0, 64), (128, 0, 64), (0, 128, 64), (128, 128, 64),
                      (0, 0, 192), (128, 0, 192), (0, 128, 192), (128, 128, 192), (64, 0, 64), (192, 0, 64),
                      (64, 128, 64), (192, 128, 64), (64, 0, 192), (192, 0, 192), (64, 128, 192), (192, 128, 192),
                      (0, 64, 64), (128, 64, 64), (0, 192, 64), (128, 192, 64), (0, 64, 192), (128, 64, 192),
                      (0, 192, 192), (128, 192, 192), (64, 64, 64), (192, 64, 64), (64, 192, 64), (192, 192, 64)]
assert len(voccontext_palette) == 60


'''voc palette'''
voc_palette = [(0, 0, 0), (128, 0, 0), (0, 128, 0), (128, 128, 0), (0, 0, 128), (128, 0, 128), 
               (0, 128, 128), (128, 128, 128), (64, 0, 0), (192, 0, 0), (64, 128, 0), (192, 128, 0), 
               (64, 0, 128), (192, 0, 128), (64, 128, 128), (192, 128, 128), (0, 64, 0), (128, 64, 0), 
               (0, 192, 0), (128, 192, 0), (0, 64, 128)]
assert len(voc_palette) == 21


'''ade20k palette'''
ade20k_palette = [(120, 120, 120), (180, 120, 120), (6, 230, 230), (80, 50, 50), (4, 200, 3), (120, 120, 80), (140, 140, 140), (204, 5, 255), (230, 230, 230), (4, 250, 7), (224, 5, 255),
                  (235, 255, 7), (150, 5, 61), (120, 120, 70), (8, 255, 51), (255, 6, 82), (143, 255, 140), (204, 255, 4), (255, 51, 7), (204, 70, 3), (0, 102, 200), (61, 230, 250),
                  (255, 6, 51), (11, 102, 255), (255, 7, 71), (255, 9, 224), (9, 7, 230), (220, 220, 220), (255, 9, 92), (112, 9, 255), (8, 255, 214), (7, 255, 224), (255, 184, 6),
                  (10, 255, 71), (255, 41, 10), (7, 255, 255), (224, 255, 8), (102, 8, 255), (255, 61, 6), (255, 194, 7), (255, 122, 8), (0, 255, 20), (255, 8, 41), (255, 5, 153),
                  (6, 51, 255), (235, 12, 255), (160, 150, 20), (0, 163, 255), (140, 140, 140), (250,  10,  15), (20, 255, 0), (31, 255, 0), (255, 31, 0), (255, 224, 0), (153, 255, 0),
                  (0, 0, 255), (255, 71, 0), (0, 235, 255), (0, 173, 255), (31, 0, 255), (11, 200, 200), (255, 82, 0), (0, 255, 245), (0,  61, 255), (0, 255, 112), (0, 255, 133),
                  (255, 0, 0), (255, 163, 0), (255, 102, 0), (194, 255, 0), (0, 143, 255), (51, 255, 0), (0, 82, 255), (0, 255, 41), (0, 255, 173), (10, 0, 255), (173, 255, 0),
                  (0, 255, 153), (255, 92, 0), (255, 0, 255), (255, 0, 245), (255, 0, 102), (255, 173, 0), (255, 0, 20), (255, 184, 184), (0, 31, 255), (0, 255, 61), (0, 71, 255),
                  (255, 0, 204), (0, 255, 194), (0, 255, 82), (0, 10, 255), (0, 112, 255), (51, 0, 255), (0, 194, 255), (0, 122, 255), (0, 255, 163), (255, 153, 0), (0, 255, 10),
                  (255, 112, 0), (143, 255, 0), (82, 0, 255), (163, 255, 0), (255, 235, 0), (8, 184, 170), (133, 0, 255), (0, 255, 92), (184, 0, 255), (255, 0, 31), (0, 184, 255),
                  (0, 214, 255), (255, 0, 112), (92, 255, 0), (0, 224, 255), (112, 224, 255), (70, 184, 160), (163, 0, 255), (153, 0, 255), (71, 255, 0), (255, 0, 163), (255, 204, 0),
                  (255, 0, 143), (0, 255, 235), (133, 255, 0), (255, 0, 235), (245, 0, 255), (255, 0, 122), (255, 245, 0), (10, 190, 212), (214, 255, 0), (0, 204, 255), (20, 0, 255),
                  (255, 255, 0), (0, 153, 255), (0, 41, 255), (0, 255, 204), (41, 0, 255), (41, 255, 0), (173, 0, 255), (0, 245, 255), (71, 0, 255), (122, 0, 255), (0, 255, 184),
                  (0, 92, 255), (184, 255, 0), (0, 133, 255), (255, 214, 0), (25, 194, 194), (102, 255, 0), (92, 0, 255)]
assert len(ade20k_palette) == 150


'''cityscapes'''
cityscapes_palette = [(128, 64, 128), (244, 35, 232), (70, 70, 70), (102, 102, 156), (190, 153, 153), (153, 153, 153), (250, 170, 30), (220, 220, 0),
                      (107, 142, 35), (152, 251, 152), (70, 130, 180), (220, 20, 60), (255, 0, 0), (0, 0, 142), (0, 0, 70), (0, 60, 100),
                      (0, 80, 100), (0, 0, 230), (119, 11, 32)]
assert len(cityscapes_palette) == 19


'''sbushadow'''
sbushadow_palette = [(0, 0, 0), (0, 0, 255)]
assert len(sbushadow_palette) == 2


'''supervisely'''
supervisely_palette = [(0, 0, 0), (0, 0, 255)]
assert len(supervisely_palette) == 2


'''collect the suppoted palettes'''
supported_palettes = {
    'voc': voc_palette,
    'lip': lip_palette,
    'cihp': cihp_palette,
    'ade20k': ade20k_palette,
    'sbushadow': sbushadow_palette,
    'cityscapes': cityscapes_palette,
    'voccontext': voccontext_palette,
    'supervisely': supervisely_palette,
}


'''build palette'''
def BuildPalette(dataset_type, **kwargs):
    assert dataset_type in supported_palettes, 'unsupport dataset_type %s...' % dataset_type
    return supported_palettes[dataset_type]