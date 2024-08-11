from pathlib import Path
from rembg import remove
import cv2

from utils import path
from utils import commindline

def remove_background():
    [input_path, output_path] = commindline.get_args()

    image_paths = path.get_file_paths_in_dir(input_path, 'png')

    for image_path in image_paths:
        background_image = cv2.imread(image_path)
        remove_background_image = remove(
            background_image,
            alpha_matting=True,
            alpha_matting_foreground_threshold=240,
            alpha_matting_background_threshold=10,
            alpha_matting_erode_structure_size=6
        )

        p_file = Path(image_path)
        cv2.imwrite(output_path+p_file.name, remove_background_image)

remove_background()