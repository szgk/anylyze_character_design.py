import json

from utils import path
from utils import image
from utils import color

def get_main_color_name_dict_by_path(input_path, exe):
    image_paths = path.get_file_paths_in_dir(input_path, exe)

    color_name_dict = {}

    # create color name dict
    for element in color.COLOR_NAMES:
        color_name_dict[str(element.value)] = []

    for image_path in image_paths:
        main_color_codes = image.get_main_color_names_by_path(image_path)

        for color_code in main_color_codes:
            rgb = color.get_RGB_from_color_code(color_code)
            color_name = color.get_color_name_from_RGB(rgb)
            color_name_dict[str(color_name.value)].append(color_code)
    
    return color_name_dict

def get_color_name_dict_by_rgb(rgb_arr):
    color_name_dict = {}

    # create color name dict
    for element in color.COLOR_NAMES:
        color_name_dict[str(element.value)] = []

    for rgb in rgb_arr:
        color_name = color.get_color_name_from_RGB(rgb)
        color_code = color.get_color_code_from_rgb(rgb)
        color_name_dict[str(color_name.value)].append(color_code)
    
    return color_name_dict


def get_color_name_chart_data(color_name_dict):
    color_name_data = color.get_dict_for_pie_chart()

    for key, value in color_name_dict.items():

      color_name_data['labels'].append(key)
      color_name_data['values'].append(len(value))
      color_name_data['colors'].append(color.get_color_code_by_color_name(key))
    
    return color_name_data

def get_color_chart_data(color_name_dict):
    color_name_data = color.get_dict_for_pie_chart()

    for key, value in color_name_dict.items():
      all_1_arr = [1 for i in range(len(value))]
      color_name_data['values'].extend(all_1_arr)
      color_name_data['colors'].extend(value)
    
    return color_name_data

def save_json(output_path, json_data):
    with open(output_path, 'w') as fp:
        json.dump(json_data, fp)