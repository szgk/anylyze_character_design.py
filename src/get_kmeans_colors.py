from PIL import Image
import cv2

from utils import image
from utils import commindline

def kmeans_colors():
    [input_path, output_path, color_nums] = commindline.get_args()

    images = image.get_images_in_dir(input_path)
    images_rgb = []
    for image_arr in images:
        rgb_arr = cv2.cvtColor(image_arr, cv2.COLOR_BGR2RGB)
        image_pil = Image.fromarray(rgb_arr)
        images_rgb.append(image_pil)

    concat_image = image.get_concat_image(images_rgb)

    main_colors = image.get_main_colors_by_image(concat_image, int(color_nums))

    main_colors_concat = image.get_concat_image(main_colors)

    main_colors_concat.save(output_path)

kmeans_colors()
