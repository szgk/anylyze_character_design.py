import cv2
import numpy
from pathlib import Path

from utils import path
from utils import commindline
from utils import image

def get_cropped_anime_face():
    [input_path, output_path, exe] = commindline.get_args()

    image_paths = path.get_file_paths_in_dir(input_path, exe)
    print(image_paths)

    face_cascade = cv2.CascadeClassifier('lib\lbpcascade_animeface.xml')

    output_width = 700
    output_height = 700

    face_area_ratio = 0.5

    for image_path in image_paths:
        p_file = Path(image_path)
        cv2_img = cv2.imread(image_path)
        _height, _width = cv2_img.shape[:2]

        faces = face_cascade.detectMultiScale(cv2_img, 1.1, 3)

        for i, (x, y, w, h) in enumerate(faces):
            mv_mat = numpy.float32([[1, 0, -x + (w * face_area_ratio)], [0, 1, -y + (h * face_area_ratio)]])
            afin_image = cv2.warpAffine(cv2_img, mv_mat, (_width, _height))
            afin_image = afin_image[0: int((h / face_area_ratio) * (output_height / output_width)), 0: int(w / face_area_ratio)]
            afin_image = cv2.resize(afin_image, dsize = (output_width, output_height))

            cv2.imwrite(output_path + p_file.stem + str(i) + '.' + exe, afin_image)

get_cropped_anime_face()  