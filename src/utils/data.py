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