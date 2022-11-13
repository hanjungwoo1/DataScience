import json
import os
import cv2
import matplotlib.pyplot as plt
from tqdm import tqdm

check_list = []


data_root_path = "../data/OCR/"
save_root_path = "../data/OCR/"

test_annotations = json.load(open('../data/OCR/test_annotation.json'))
with open(save_root_path + "gt_test.txt", 'w', encoding="utf-8") as gt_file:
    for file_name in tqdm(test_annotations):
        annotations = test_annotations[file_name]
        image = cv2.imread(data_root_path+ "/test/img"+file_name[5:])

        for idx, annotation in enumerate(annotations):
            x, y, w, h = annotation['annotation.bbox']
            if x<=0 or y<=0 or w<=0 or h<=0:
                check_list.append((file_name, idx))
                continue
            text = annotation['annotation.text']
            crop_img = image[y:y+h, x:x+w]
            crop_file_name = file_name[:-4]+'_{:03}.jpg'.format(idx+1)
            cv2.imwrite(save_root_path + 'test_processed/' + crop_file_name, crop_img)
            gt_file.write("test/{}\t{}\n".format(crop_file_name, text))
#
#
# valid_annotations = json.load(open('../data/OCR/valid_annotation.json'))
# with open(save_root_path + "gt_valid.txt", 'w', encoding="utf-8") as gt_file:
#     for file_name in tqdm(valid_annotations):
#         annotations = valid_annotations[file_name]
#         image = cv2.imread(data_root_path+ "/valid/img"+file_name[5:])
#
#         for idx, annotation in enumerate(annotations):
#             x, y, w, h = annotation['annotation.bbox']
#             if x<=0 or y<=0 or w<=0 or h<=0:
#                 check_list.append((file_name, idx))
#                 continue
#             text = annotation['annotation.text']
#             crop_img = image[y:y+h, x:x+w]
#             crop_file_name = file_name[:-4]+'_{:03}.jpg'.format(idx+1)
#             cv2.imwrite(save_root_path + 'valid_processed/' + crop_file_name, crop_img)
#             gt_file.write("valid/{}\t{}\n".format(crop_file_name, text))


# train_annotations = json.load(open('../data/OCR/train_annotation.json'))
# with open(save_root_path + "gt_train.txt", 'w', encoding="utf-8") as gt_file:
#     for file_name in tqdm(train_annotations):
#         annotations = train_annotations[file_name]
#         image = cv2.imread(data_root_path+ "/train/img"+file_name[5:])
#
#         for idx, annotation in enumerate(annotations):
#             x, y, w, h = annotation['annotation.bbox']
#             if x<=0 or y<=0 or w<=0 or h<=0:
#                 check_list.append((file_name, idx))
#                 continue
#             text = annotation['annotation.text']
#             crop_img = image[y:y+h, x:x+w]
#             crop_file_name = file_name[:-4]+'_{:03}.jpg'.format(idx+1)
#             cv2.imwrite(save_root_path + 'train_processed/' + crop_file_name, crop_img)
#             gt_file.write("train/{}\t{}\n".format(crop_file_name, text))
