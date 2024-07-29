from utils import path
from pathlib import Path
from PIL import Image
from sklearn.cluster import KMeans
import numpy as np
from utils import image
import cv2

def kmeans_main_colors():
    images = image.get_images_in_dir('./output/main_colors')
    images_rgb = []
    for image_arr in images:
        rgb_arr = cv2.cvtColor(image_arr, cv2.COLOR_BGR2RGB)
        image_pil = Image.fromarray(rgb_arr)
        images_rgb.append(image_pil)

    concat_image = image.get_concat_image(images_rgb)

    main_colors = image.get_main_colors_by_image(concat_image, 40)

    main_colors_concat = image.get_concat_image(main_colors)

    main_colors_concat.save('./output/main_colors_concat.jpg')

kmeans_main_colors()
