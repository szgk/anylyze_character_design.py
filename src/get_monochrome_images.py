import numpy
import sys
import cv2
import dlib
from pathlib import Path

from utils import path
from utils import commindline
from utils import image

# こちらのコードを参考にさせて頂いています
# https://github.com/marron-akanishi/AFD/blob/master/sample.py

def get_monochrome_images():
    [input_path, output_path, exe] = commindline.get_args()

    image_paths = path.get_file_paths_in_dir(input_path, exe)
    print(image_paths)

    for image_path in image_paths:
        print(image_path)
        cv2_img = cv2.imread(image_path)
        img_gry = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)

        p_file = Path(image_path)
        _output_path = output_path + p_file.stem + '.' + exe
    
        ret, img_thresh = cv2.threshold(img_gry, 0, 255, cv2.THRESH_OTSU)

        cv2.imwrite(_output_path, img_thresh)

get_monochrome_images()  