from utils import path
from pathlib import Path

from utils import image
from utils import commindline

def get_per_mian_colors():
    [input_path, output_path] = commindline.get_args()

    image_paths = path.get_file_paths_in_dir(input_path, 'png')
    for image_path in image_paths:
        main_color_images = image.get_main_colors_by_path(image_path)
        p_file = Path(image_path)
        for i, _image in enumerate(main_color_images):
            _image.save(output_path+'/'+p_file.stem+'_'+str(i)+p_file.suffix)

get_per_mian_colors()