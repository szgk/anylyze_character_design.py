import copy
import re
import json
from utils import commindline

def merge_avatar_face_raito_and_like():
    [face_ratio_data, avatar_data, output_path] = commindline.get_args()
    ratio_dict = json.load(open(face_ratio_data))
    avatar_data = json.load(open(avatar_data, encoding="utf-8"))

    result = {}

    for key, value in ratio_dict.items():
        if len(ratio_dict[key].items()) == 0: continue
        result[key] = value
        result[key]['like'] =0
        for avatar_info in avatar_data:
            if(avatar_info['data_id'] == re.sub(r'_.*', '', key)):
                result[key]['like'] = int(avatar_info['like'])
                

    with open(output_path, 'w', encoding="utf-8") as f:
        print('save json')
        json.dump(result, f, ensure_ascii=False)

merge_avatar_face_raito_and_like()