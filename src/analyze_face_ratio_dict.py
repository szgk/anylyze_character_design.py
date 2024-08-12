import json
import math

from utils import path
from utils import commindline

def analyze_face_ratio_dict():
    [input_path, output_path] = commindline.get_args()

    result = {
        'eye_big': {
            'name': '',
            'num': 0
        },
        'eye_small': {
            'name': '',
            'num': 99999
        },
        'eye_distance_wide': {
            'name': '',
            'num': 0
        },
        'eye_distance_narrow': {
            'name': '',
            'num': 99999
        },
        'eye_to_side_wide': {
            'name': '',
            'num': 0
        },
        'eye_to_side_short': {
            'name': '',
            'num': 99999
        },
        'forehead_long': {
            'name': '',
            'num': 0
        },
        'forehead_short': {
            'name': '',
            'num': 99999
        },
        'face_bottom_long': {
            'name': '',
            'num': 0
        },
        'face_bottom_short': {
            'name': '',
            'num': 99999
        },
        'eye_height_average': 0,
        'eye_width_average': 0,
        'eye_to_eye_average': 0,
        'forehead_average': 0,
        'face_bottom_average': 0,
        'eye_to_side_average': 0,
    }

    # {
    #     "vketchan_0": {
    #         "face_width": 52,
    #         "face_height": 52,
    #         "eye_count": 1,
    #         "eye_height": 0.3076923076923077,
    #         "eye_width": 0.38461538461538464,
    #         "eye_to_eye": 0,
    #         "eye_to_side": 0.6346153846153846,
    #         "eye_to_jaw": 0.6538461538461539,
    #         "eye_to_forehead": 0.34615384615384615
    #     }
    # }
    ratio_dict = json.load(open(input_path, 'r'))
    print(ratio_dict)
    items = ratio_dict.items()

    eye_height_total = 0
    eye_width_total = 0
    eye_to_eye_total = 0
    forehead_total = 0
    face_bottom_total = 0
    eye_to_side_total = 0
    length = len(items)


    for key, value in items:
        print(value)
        print(len(value.items()))
        if(len(value.items()) == 0):
            continue
        
        eye_height = math.floor(value['eye_height'] * 100)
        eye_width = math.floor(value['eye_width'] * 100)
        eye_to_eye = math.floor(value['eye_to_eye'] * 100)
        forehead = math.floor(value['eye_to_forehead'] * 100)
        face_bottom = math.floor(value['eye_to_jaw'] * 100)
        eye_to_side = math.floor(value['eye_to_side'] * 100)

        eye_height_total += value['eye_height'] 
        eye_width_total += value['eye_width'] 
        eye_to_eye_total += value['eye_to_eye'] 
        forehead_total += value['eye_to_forehead'] 
        face_bottom_total += value['eye_to_jaw'] 
        eye_to_side_total += value['eye_to_side'] 

        if (result['eye_big']['num'] < eye_height*eye_width):
            result['eye_big']['name'] = key
            result['eye_big']['num'] = eye_height*eye_width
        if ((eye_height*eye_width > 0) and result['eye_small']['num'] > eye_height*eye_width):
            result['eye_small']['name'] = key
            result['eye_small']['num'] = eye_height*eye_width

        if (result['eye_distance_wide']['num'] < eye_to_eye):
            result['eye_distance_wide']['name'] = key
            result['eye_distance_wide']['num'] = eye_to_eye
        if (eye_to_eye > 0 and result['eye_distance_narrow']['num'] > eye_to_eye):
            result['eye_distance_narrow']['name'] = key
            result['eye_distance_narrow']['num'] = eye_to_eye

        if (result['eye_to_side_wide']['num'] < eye_to_side):
            result['eye_to_side_wide']['name'] = key
            result['eye_to_side_wide']['num'] = eye_to_side
        if (eye_to_side > 0 and result['eye_to_side_short']['num'] > eye_to_side):
            result['eye_to_side_short']['name'] = key
            result['eye_to_side_short']['num'] = eye_to_side

        if (result['forehead_long']['num'] < forehead):
            result['forehead_long']['name'] = key
            result['forehead_long']['num'] = forehead
        if (forehead > 0 and result['forehead_short']['num'] > forehead):
            result['forehead_short']['name'] = key
            result['forehead_short']['num'] = forehead

        if (result['face_bottom_long']['num'] < face_bottom):
            result['face_bottom_long']['name'] = key
            result['face_bottom_long']['num'] = face_bottom
        if (face_bottom > 0 and result['face_bottom_short']['num'] > face_bottom):
            result['face_bottom_short']['name'] = key
            result['face_bottom_short']['num'] = face_bottom

    eye_height_total = math.floor(eye_height_total * 1000) / 1000
    eye_width_total = math.floor(eye_width_total * 1000) / 1000
    eye_to_eye_total = math.floor(eye_to_eye_total * 1000) / 1000
    forehead_total = math.floor(forehead_total * 1000) / 1000
    face_bottom_total = math.floor(face_bottom_total * 1000) / 1000
    eye_to_side_total = math.floor(eye_to_side_total * 1000) / 1000

    result['eye_height_average'] = eye_height_total / length
    result['eye_width_average'] = eye_width_total / length
    result['eye_to_eye_average'] = eye_to_eye_total / length
    result['forehead_average'] = forehead_total / length
    result['face_bottom_average'] = face_bottom_total / length
    result['eye_to_side_average'] = eye_to_side_total / length

    with open(output_path, 'w') as fp:
        json.dump(result, fp)

analyze_face_ratio_dict()  