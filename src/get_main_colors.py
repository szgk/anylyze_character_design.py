from utils import path
from pathlib import Path
from PIL import Image
from sklearn.cluster import KMeans
import numpy as np
from utils import image

def get_main_colors():
    image_paths = path.get_file_paths_in_dir('./output/images')

    for image_path in image_paths:
        main_color_images = image.get_main_colors_by_path(image_path)
        concat_image = image.get_concat_image(main_color_images)
        p_file = Path(image_path)
        concat_image.save('./output/main_colors/'+p_file.name)

get_main_colors()