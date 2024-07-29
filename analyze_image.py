from pathlib import Path 
import PIL
from PIL import Image
import cv2
import sklearn
from sklearn.cluster import KMeans
import numpy as np

def exec():
    image_paths = get_file_paths_in_dir('./images')
    for image_path in image_paths:
        main_color_images = get_main_color_arr(image_path)
        concat_image = get_concat_image(main_color_images)
        p_file = Path(image_path)
        concat_image.save('./main_colors/'+p_file.name)

def get_main_color_arr(path, num = 5):
    cv2_img = cv2.imread(path)
    cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)

    cv2_img = cv2_img.reshape(
        (cv2_img.shape[0] * cv2_img.shape[1], 3))

    cv2_img.shape

    print(cv2_img.shape)

    cluster = KMeans(n_clusters=num)

    cluster.fit(X=cv2_img)

    KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
        n_clusters=5, n_init=10,
        random_state=None, tol=0.0001, verbose=0)

    cluster.cluster_centers_

    cluster_centers_arr = cluster.cluster_centers_.astype(
        int, copy=False)

    print(cluster_centers_arr.shape)

    i = 0
    image_arr = []
    for rgb_arr in cluster_centers_arr:
        color_hex_str = '#%02x%02x%02x' % tuple(rgb_arr)
        print(color_hex_str)
        color_img = Image.new(
            mode='RGB', size=(32, 32), color=color_hex_str)
        print(color_img)
        image_arr.append(color_img)

    return image_arr

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

def get_file_paths_in_dir(path, ex = "jpg"):
    input_dir = path
    input_list = list(Path(input_dir).glob('**/*.'+ex))
    return input_list

exec()