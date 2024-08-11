from PIL import Image
import cv2
import sklearn
from sklearn.cluster import KMeans
import numpy as np
from pathlib import Path
from utils import path

def get_images_in_dir(dir):
    image_paths = path.get_file_paths_in_dir(dir)
    images = []
    for image_path in image_paths:
        image = cv2.imread(image_path)
        images.append(image)
    
    return images

def get_cluster_centers_arr(cv2img, num = 5):
    cv2_img = cv2.cvtColor(cv2img, cv2.COLOR_BGR2RGB)

    cv2_img = cv2_img.reshape(
        (cv2_img.shape[0] * cv2_img.shape[1], 3))

    cluster = KMeans(n_clusters=num)

    cluster.fit(X=cv2_img)

    KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
        n_clusters=5, n_init=10,
        random_state=None, tol=0.0001, verbose=0)

    cluster.cluster_centers_

    cluster_centers_arr = cluster.cluster_centers_.astype(
        int, copy=False)
    
    return cluster_centers_arr

def get_main_colors_from_cv2img(cv2img, num = 5):
    cluster_centers_arr = get_cluster_centers_arr(cv2img, num)

    image_arr = []
    for rgb_arr in cluster_centers_arr:
        color_hex_str = '#%02x%02x%02x' % tuple(rgb_arr)
        color_img = Image.new(
            mode='RGB', size=(32, 32), color=color_hex_str)
        image_arr.append(color_img)

    return image_arr

def get_main_color_names_from_cv2img(cv2img, num = 5):
    cluster_centers_arr = get_cluster_centers_arr(cv2img, num)

    name_arr = []
    for rgb_arr in cluster_centers_arr:
        color_hex_str = '#%02x%02x%02x' % tuple(rgb_arr)
        name_arr.append(color_hex_str)

    return name_arr

def get_main_colors_by_path(path, num = 5):
    cv2_img = cv2.imread(path)
    return get_main_colors_from_cv2img(cv2_img, num)

def get_main_color_names_by_path(path, num = 5):
    cv2_img = cv2.imread(path)
    return get_main_color_names_from_cv2img(cv2_img, num)

def get_main_colors_by_image(image, num = 5):
    cv2_img = np.array(image.convert('RGB'))
    return get_main_colors_from_cv2img(cv2_img, num)


def get_concat_image(images):
    image_width = 0
    image_height_nums = []

    for im in images:
        image_width += im.width

    for im in images:
        image_height_nums.append(im.height)

    images_height = np.amax(np.array(image_height_nums))

    concat_image = Image.new('RGB', (image_width, images_height))

    current_width = 0
    for i, im in enumerate(images):
        concat_image.paste(im, (current_width, 0))
        current_width += im.width

    return concat_image