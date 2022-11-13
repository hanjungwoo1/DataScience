import json


train_annotations = json.load(open('../data/OCR/train_annotation.json'))
print(len(train_annotations.keys()))

count = 0
for file_name in train_annotations:
    annotations = train_annotations[file_name]
    for idx, annotation in enumerate(annotations):
        count += 1

print(count)