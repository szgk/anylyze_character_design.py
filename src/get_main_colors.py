from utils import path
from pathlib import Path

from utils import image
from utils import commindline

def get_main_colors():
    [input_path, output_path, exe] = commindline.get_args()

    image_paths = path.get_file_paths_in_dir(input_path, exe)

    for image_path in image_paths:
        print(image_path)
        main_color_images = image.get_main_colors_by_path(image_path)
        concat_image = image.get_concat_image(main_color_images)
        p_file = Path(image_path)
        concat_image.save(output_path+p_file.name)

get_main_colors()