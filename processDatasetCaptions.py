# -*- encoding = utf8 -*-
# @Time : 2024/9/24 13:59
# @Author : Zed
# @File : processText.py
# @Software : PyCharm
import json

json_file_path = 'data/coco2017val/annotations_trainval2017/captions_val2017.json'
output_dir = 'data/coco2017val/val2017_captions/'

# 打开文件
with open(json_file_path, 'r', encoding='utf-8') as file:
    # 加载 JSON 数据
    data = json.load(file)

    if isinstance(data, dict):
        files_dict = dict()
        for image in data['images']:
            files_dict[image["id"]] = {"file_name": image["file_name"], "captions": []}
        for annotation in data['annotations']:
            files_dict[annotation['image_id']]["captions"].append(annotation['caption'])
        for value in files_dict.values():
            with open(output_dir + value['file_name'].replace('jpg','txt'), 'w', encoding='utf-8') as file:
                # 写入数据到文件
                for caption in value['captions']:
                    file.write(caption + '\n')
