import os
import json
import shutil

from PIL import Image
from torch.utils.data import Dataset
from sklearn.model_selection import train_test_split


class RawDataset(Dataset):
    def __init__(self, root):
        self.image_path_list = []
        self.image_list = []
        for dirpath, dirnames, filenames in os.walk(root):
            for name in filenames:
                _, ext = os.path.splitext(name)
                ext = ext.lower()
                if ext == '.jpg' or ext == '.jpeg' or ext == '.png':
                    self.image_path_list.append(os.path.join(dirpath, name))

        # self.image_path_list = natsorted(self.image_path_list)
        self.nSamples = len(self.image_path_list)

    def __len__(self):
        # return self.nSamples
        return len(self.image_list)

    def __getitem__(self, index):

        try:
            img = Image.open(self.image_list[index]).convert('L')

        except IOError:
            print(f'Corrupted image for {index}')
            # make dummy image and dummy label for corrupted image.
            img = Image.new('L', (100, 32))

        return (img, self.image_list[index])

class JsonDataset(Dataset):
    def __init__(self, root):
        self.json_path_list = []
        self.json_list = []
        for dirpath, dirnames, filenames in os.walk(root):
            for name in filenames:
                _, ext = os.path.splitext(name)
                ext = ext.lower()
                if ext == '.json':
                    self.json_path_list.append(os.path.join(dirpath, name))

        # self.image_path_list = natsorted(self.image_path_list)
        self.nSamples = len(self.json_path_list)

    def __len__(self):
        # return self.nSamples
        return len(self.json_list)

    def __getitem__(self, index):

        try:
            with open(self.json_list[index], 'r', encoding='UTF-8') as f:
                json_data = json.load(f)
        except IOError:
            print(f'Corrupted image for {index}')

        print(json_data)
        annotation = [ a for a in json_data["annotations"]]
        return annotation



imgs = RawDataset("../data/공공행정문서 OCR/Validation/[원천]validation")
labels = JsonDataset("../data/공공행정문서 OCR/Validation/[라벨]validation")

print(len(imgs.image_path_list))
print(len(labels.json_path_list))

count = 0

for x, y in zip(imgs.image_path_list, labels.json_path_list):

    split_x = x.split("\\")[-1][:-4]
    split_y = y.split("\\")[-1][:-5]

    if split_x == split_y:
        imgs.image_list.append((x))
        labels.json_list.append((y))


train_imgs, valid_test_img, train_labels, valid_test_labels = train_test_split(imgs.image_list, labels.json_list, test_size=0.3, random_state=940107)
print(len(train_imgs), len(valid_test_img), len(train_labels), len(valid_test_labels))

val_imgs, test_imgs, val_labels, test_labels = train_test_split(valid_test_img, valid_test_labels, test_size=0.5, random_state=940107)
print(len(val_imgs), len(test_imgs), len(val_labels), len(test_labels))

print(labels.__getitem__(0))
print(labels.json_list[0])

def move_files(img_list, label_list, destination_path):

    count = 1
    for img, label in zip(img_list, label_list):
        img_path = destination_path + "/img" + str(count) + ".JPG"
        label_path = destination_path + "/label" + str(count) + ".json"
        shutil.copy(img, img_path)
        shutil.copy(label, label_path)
        count += 1
    return

move_files(train_imgs, train_labels, "../data/OCR/train")
move_files(val_imgs, val_labels, "../data/OCR/valid")
move_files(test_imgs, test_labels, "../data/OCR/test")