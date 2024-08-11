from utils import path
from pathlib import Path
import json

from utils import image
from utils import commindline

def get_main_color_codes():
    [input_path, output_path] = commindline.get_args()

    image_paths = path.get_file_paths_in_dir(input_path, 'png')

    main_color_dict = {}

    for image_path in image_paths:
        main_color_names = image.get_main_color_names_by_path(image_path)
        p_file = Path(image_path)
        colors_arr = []

        for _image in main_color_names:
            colors_arr.append(_image)

        main_color_dict[p_file.stem] = colors_arr

    with open(output_path, 'w') as fp:
        json.dump(main_color_dict, fp)
        

get_main_color_codes()