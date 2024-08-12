from PIL import Image
from pathlib import Path

from utils import path
from utils import commindline
from utils import chart
from utils import color
from utils import image
from utils import data

def get_color_rgb():
    [input_path, output_path, exe] = commindline.get_args()

    image_paths = path.get_file_paths_in_dir(input_path, exe)

    for image_path in image_paths:
        print('start image_path')
        p_file = Path(image_path)
        _output_path = output_path+p_file.stem+'.json'
        print('output_path:', _output_path)
        # compress image
        print('start get_color_from_path')
        rgb_arr = image.get_color_from_path(image_path, 700)
        print('start get_color_name_dict_by_rgb')
        color_name_dict = data.get_color_name_dict_by_rgb(rgb_arr)
        print('start save_json')

        data.save_json(_output_path, color_name_dict)

get_color_rgb()
