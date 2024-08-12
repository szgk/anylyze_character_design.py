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

def get_anime_face_rate_AFD():
    [input_path, output_path, exe] = commindline.get_args()

    image_paths = path.get_file_paths_in_dir(input_path, exe)
    print(image_paths)

    face_detector = dlib.simple_object_detector("./lib/detector_face.svm")
    eye_detector = dlib.simple_object_detector("./lib/detector_eye.svm")


    for image_path in image_paths:
        print(image_path)
        cv2_img = cv2.imread(image_path)
        p_file = Path(image_path)
        _output_path = output_path + p_file.stem + '.' + exe

        print(_output_path)
    
        faces = face_detector(cv2_img)
  
        for rect in faces:

            x_start = rect.left()
            x_end = rect.right()
            y_start = rect.top()
            y_end = rect.bottom()

            face_width = x_end - x_start
            face_height = y_end - y_start

            if abs(face_width - face_height) > 3:
                continue

            face = cv2_img[y_start:y_end, x_start:x_end]

            eyes = eye_detector(face)
            if len(eyes) > 0:
                for eye in eyes:
                    cv2.rectangle(cv2_img, (x_start+eye.left(), y_start+eye.top()),
                                (x_start+eye.right(), y_start+eye.bottom()), (255, 0, 0), thickness=2)
            else:
                continue

            cv2.rectangle(cv2_img, (x_start, y_start), (x_end, y_end), (0, 0, 255), thickness=2)

        # 顔部分を赤線で囲った画像の保存
        cv2.imwrite(_output_path, cv2_img)

get_anime_face_rate_AFD()  