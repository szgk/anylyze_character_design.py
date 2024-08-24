from PIL import Image
from pathlib import Path
import json

from utils import path
from utils import commindline
from utils import image
from utils import data
from utils import regex

def get_color_json_for_pi_chart_by_dir(input_path, output_path, exe):
    [input_path, output_path, exe] = commindline.get_args()

    image_paths = path.get_file_paths_in_dir(input_path, exe)

    for image_path in image_paths:
        print(image_path)
        p_file = Path(image_path)
        # _output_path = output_path+p_file.name

        # compress image
        print('start get_color_from_path')
        rgb_arr = image.get_color_from_path(image_path, 700)

        print('start get_color_name_dict_by_rgb')
        color_name_dict = data.get_color_name_dict_by_rgb(rgb_arr)

        with open(output_path+'color_name_dict/'+p_file.stem+'.json', 'w') as fp:
            json.dump(color_name_dict, fp)

        print('start get_color_name_chart_data')
        chart_data1 = data.get_color_name_chart_data(color_name_dict)

        with open(output_path+'chart_data1/'+p_file.stem+'.json', 'w') as fp:
            json.dump(chart_data1, fp)

        print('start get_color_chart_data')
        chart_data2 = data.get_color_chart_data(color_name_dict)

        with open(output_path+'chart_data2/'+p_file.stem+'.json', 'w') as fp:
            json.dump(chart_data2, fp)

def get_color_json_for_pi_chart_by_file(input_path, output_path):
    print(input_path)
    p_file = Path(input_path)

    # compress image
    print('start get_color_from_path')
    rgb_arr = image.get_color_from_path(input_path, 700)

    print('start get_color_name_dict_by_rgb')
    color_name_dict = data.get_color_name_dict_by_rgb(rgb_arr)

    with open(output_path+'color_name_dict/'+p_file.stem+'.json', 'w') as fp:
        json.dump(color_name_dict, fp)

    print('start get_color_name_chart_data')
    chart_data1 = data.get_color_name_chart_data(color_name_dict)

    with open(output_path+'chart_data1/'+p_file.stem+'.json', 'w') as fp:
        json.dump(chart_data1, fp)

    print('start get_color_chart_data')
    chart_data2 = data.get_color_chart_data(color_name_dict)

    with open(output_path+'chart_data2/'+p_file.stem+'.json', 'w') as fp:
        json.dump(chart_data2, fp)

def get_color_json_for_pi_chart():
    [input_path, output_path, exe] = commindline.get_args()

    if(regex.is_file_path(input_path)):
        get_color_json_for_pi_chart_by_file(input_path, output_path)
    else:
        get_color_json_for_pi_chart_by_dir(input_path, output_path, exe)


get_color_json_for_pi_chart()
