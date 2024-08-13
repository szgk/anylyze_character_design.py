from utils import path
import json

from utils import commindline
from utils import data

def get_main_color_names():
    [input_path, output_path, exe] = commindline.get_args()

    color_name_dict = data.get_main_color_name_dict_by_path(input_path, exe)

    with open(output_path, 'w') as fp:
        json.dump(color_name_dict, fp)
        

get_main_color_names()