import math
import json
import numpy as np
import matplotlib.pyplot as plt

from utils import commindline
from utils import sort
from utils import chart

def get_face_ratio_chart():
    [input_path, output_path] = commindline.get_args()
    face_ratio_dict = json.load(open(input_path, 'r'))

    face_width_dict = {}
    face_height_dict = {}
    eye_height_dict = {}
    eye_width_dict = {}
    eye_to_side_dict = {}
    eye_to_jaw_dict = {}
    eye_to_forehead_dict = {}
    eye_to_eye_dict = {}

    # face_width, face_height, eye_count, eye_height, eye_width, eye_to_eye, eye_to_side, eye_to_jaw, eye_to_forehead
    for avatar_name, ratio in face_ratio_dict.items():
        if(len(ratio.keys()) == 0): continue
        face_width_dict[avatar_name] = math.floor((ratio['face_width'] / ratio['face_height'])*100)/100
        face_height_dict[avatar_name] = math.floor((ratio['face_height'] / ratio['face_width'])*100)/100
        if(ratio['eye_height'] >  0): eye_height_dict[avatar_name] = ratio['eye_height']
        if(ratio['eye_width'] >  0): eye_width_dict[avatar_name] = ratio['eye_width']
        if(ratio['eye_to_side'] >  0): eye_to_side_dict[avatar_name] = ratio['eye_to_side']
        if(ratio['eye_to_jaw'] >  0):eye_to_jaw_dict[avatar_name] = ratio['eye_to_jaw']
        if(ratio['eye_to_forehead'] >  0): eye_to_forehead_dict[avatar_name] = ratio['eye_to_forehead']
        if(ratio['eye_count'] >  1): eye_to_eye_dict[avatar_name] = abs(ratio['eye_to_eye'])

    sorted_face_width_dict = sort.dict_by_value(face_width_dict)
    sorted_face_height_dict = sort.dict_by_value(face_height_dict)
    sorted_eye_height_dict = sort.dict_by_value(eye_height_dict)
    sorted_eye_width_dict = sort.dict_by_value(eye_width_dict)
    sorted_eye_height_dict = sort.dict_by_value(eye_height_dict)
    sorted_eye_to_side_dict = sort.dict_by_value(eye_to_side_dict)
    sorted_eye_to_jaw_dict = sort.dict_by_value(eye_to_jaw_dict)
    sorted_eye_to_forehead_dict = sort.dict_by_value(eye_to_forehead_dict)
    sorted_eye_to_eye_dict= sort.dict_by_value(eye_to_eye_dict)

    chart.get_bar_graph(output_path + 'sorted_face_width_dict.png', list(sorted_face_width_dict.keys()), list(sorted_face_width_dict.values()))
    chart.get_bar_graph(output_path + 'sorted_face_height_dict.png', list(sorted_face_height_dict.keys()), list(sorted_face_height_dict.values()))
    chart.get_bar_graph(output_path + 'sorted_eye_height_dict.png', list(sorted_eye_height_dict.keys()), list(sorted_eye_height_dict.values()))
    chart.get_bar_graph(output_path + 'sorted_eye_height_dict.png', list(sorted_eye_height_dict.keys()), list(sorted_eye_height_dict.values()))
    chart.get_bar_graph(output_path + 'sorted_eye_width_dict.png', list(sorted_eye_width_dict.keys()), list(sorted_eye_width_dict.values()))
    chart.get_bar_graph(output_path + 'sorted_eye_to_side_dict.png', list(sorted_eye_to_side_dict.keys()), list(sorted_eye_to_side_dict.values()))
    chart.get_bar_graph(output_path + 'sorted_eye_to_jaw_dict.png', list(sorted_eye_to_jaw_dict.keys()), list(sorted_eye_to_jaw_dict.values()))
    chart.get_bar_graph(output_path + 'sorted_eye_to_forehead_dict.png', list(sorted_eye_to_forehead_dict.keys()), list(sorted_eye_to_forehead_dict.values()))
    chart.get_bar_graph(output_path + 'sorted_eye_to_eye_dict.png', list(sorted_eye_to_eye_dict.keys()), list(sorted_eye_to_eye_dict.values()))


get_face_ratio_chart()