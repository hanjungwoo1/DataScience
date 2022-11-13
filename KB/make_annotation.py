import os
import json


train_img_ids = {}
validation_img_ids = {}
test_img_ids = {}


def find_jsons(root):
    file_list = []
    for dirpath, _, filenames in os.walk(root):
        for files in filenames:
            if ".json" in str(files):
                file_list.append(files)



    return dirpath, file_list

root_path, train_list = find_jsons("../data/OCR/train")
root_path, valid_list = find_jsons("../data/OCR/valid")
root_path, test_list = find_jsons("../data/OCR/test")

print(root_path)

def make_annotation_json(path:str, file_list:list, train_img_ids:dict):

    count = 0
    for file in file_list:
        file_path = path + "/" + file
        try:
            with open(file_path, 'r', encoding='UTF-8') as f:
                json_data = json.load(f)

        except IOError:
            print(f'Corrupted image for {file}')

        img_names = file[:-5] + ".jpg"

        train_img_ids[img_names] = json_data["annotations"]
        count += 1

        if count == 5:
            break

make_annotation_json(root_path, train_list, train_img_ids)
make_annotation_json(root_path, valid_list, validation_img_ids)
make_annotation_json(root_path, test_list, test_img_ids)


with open('../data/OCR/train_annotation.json', 'w') as file:
    json.dump(train_img_ids, file)

with open('../data/OCR/valid_annotation.json', 'w') as file:
    json.dump(validation_img_ids, file)

with open('../data/OCR/test_annotation.json', 'w') as file:
    json.dump(test_img_ids, file)
