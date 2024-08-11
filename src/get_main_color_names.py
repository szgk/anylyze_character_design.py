from utils import path
from pathlib import Path
import json

from utils import image
from utils import color
from utils import commindline

def get_main_color_names():
    [input_path, output_path, exe] = commindline.get_args()

    image_paths = path.get_file_paths_in_dir(input_path, exe)

    print(image_paths)

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


    print(color_name_dict)

    with open(output_path, 'w') as fp:
        json.dump(color_name_dict, fp)
        

get_main_color_names()