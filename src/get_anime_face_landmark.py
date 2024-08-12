import numpy
import sys
import cv2
import dlib
from pathlib import Path
from imutils import face_utils

from utils import path
from utils import commindline
from utils import image


def get_anime_face_landmark():
    [input_path, output_path, exe] = commindline.get_args()

    image_paths = path.get_file_paths_in_dir(input_path, exe)
    print(image_paths)

    face_detector = dlib.simple_object_detector("./lib/detector_face.svm")
    face_predictor = dlib.shape_predictor('./lib/shape_predictor_68_face_landmarks.dat')


    for image_path in image_paths:
        print(image_path)
        cv2_img = cv2.imread(image_path)
        img_gry = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)

        p_file = Path(image_path)
        _output_path = output_path + p_file.stem + '.' + exe

        print(_output_path)
    
        faces = face_detector(img_gry)

        for face in faces:
            landmark = face_predictor(img_gry, face)
            landmark = face_utils.shape_to_np(landmark)

            # ランドマーク描画
            for (i, (x, y)) in enumerate(landmark):
                cv2.circle(cv2_img, (x, y), 1, (255, 0, 0), -1)
        
        cv2.imwrite(_output_path, cv2_img)

get_anime_face_landmark()  