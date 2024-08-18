import re
import json
from utils import commindline

# src\get_anime_face_ratio.py
#  face_ratio_data
# {
#   "adolescentu_0": {
#     "face_width": 90,
#     "face_height": 90,
#     "eye_count": 0,
#     "eye_height": 0,
#     "eye_width": 0,
#     "eye_to_eye": 0,
#     "eye_to_side": 0,
#     "eye_to_jaw": 0,
#     "eye_to_forehead": 0
# }

#  https://docs.google.com/spreadsheets/d/11egC88d7PB18CPwUlaHlPIH6pgVHsR_qLlzRESh15UI/edit?gid=0#gid=0
#  avatar_data
# [
#     {
#         "about_sale_date": "2022/02/26",
#         "name": "aa",
#         "data_id": "aaa",
#         "author": "aa",
#         "like": "21118",
#         "url": "https://booth.pm/ja/items/aaa",
#         "category": "少女",
#         "about_polygon": "108686",
#         "body": "中",
#         "chest": "大",
#         "kemomimi": "",
#         "tail": "",
#         "horn": "",
#         "wing": "",
#         "elfmimi": "",
#         "hairo": "",
#         "robo": ""
#     },
# ]

def merge_avatar_data_and_face_raito_data():
    [face_ratio_data, avatar_data, output_path] = commindline.get_args()
    ratio_dict = json.load(open(face_ratio_data))
    avatar_data = json.load(open(avatar_data, encoding="utf-8"))

    result = {}
    avatar_keys = []

    for value in avatar_data:
        data_id = value['data_id']
        avatar_keys.append(data_id)
        value['face_raito'] = []

        result[data_id] = value

    for key, value in ratio_dict.items():
        print(key)

        for avatar_key in avatar_keys:
            if(avatar_key == re.sub(r'_.*', '', key)):
                if('eye_count' in ratio_dict[key] and ratio_dict[key]['eye_count'] > 0):
                   result[avatar_key]['face_raito'].append(ratio_dict[key])

    with open(output_path, 'w', encoding="utf-8") as f:
        print('save json')
        json.dump(result, f, ensure_ascii=False)

merge_avatar_data_and_face_raito_data()