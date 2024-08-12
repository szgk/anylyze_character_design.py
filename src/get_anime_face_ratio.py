import json
import cv2
import dlib
import copy
from pathlib import Path

from utils import path
from utils import commindline

def get_anime_face_ratio():
    [input_path, output_path, exe] = commindline.get_args()

    image_paths = path.get_file_paths_in_dir(input_path, exe)
    print(image_paths)

    face_detector = dlib.simple_object_detector("./lib/detector_face.svm")
    eye_detector = dlib.simple_object_detector("./lib/detector_eye.svm")

    result = {}

    for image_path in image_paths:
        print(image_path)
        cv2_img = cv2.imread(image_path)
        img_gry = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)

        p_file = Path(image_path)

        faces = face_detector(img_gry)
  
        for i, rect in enumerate(faces):

            face_left = rect.left()
            face_right = rect.right()
            face_top = rect.top()
            face_bottom = rect.bottom()

            face_width = face_right - face_left
            face_height = face_bottom - face_top

            if abs(face_width - face_height) > 3:
                continue

            face = cv2_img[face_top:face_bottom, face_left:face_right]

            eyes = eye_detector(face)

            eye_count = len(eyes)

            face_rect_dict = {
                'face_width': face_width,
                'face_height': face_height,
                'eye_count': eye_count,
                'eye_height': 0,
                'eye_width': 0,
                'eye_to_eye': 0,
                'eye_to_side': 0,
                'eye_to_jaw': 0,
                'eye_to_forehead': 0,
            }

            result[p_file.stem + '_' + str(i)] = copy.deepcopy(face_rect_dict)

            # 目検出時
            if eye_count > 0:
                eye1 = eyes[0]
                eye_width = eye1.right() - eye1.left()
                eye_height = eye1.bottom() - eye1.top()

                face_rect_dict['eye_width'] = eye_width / face_width
                face_rect_dict['eye_height'] = eye_height / face_height
                face_rect_dict['eye_to_jaw'] = eye1.bottom() / face_height
                face_rect_dict['eye_to_forehead'] = eye1.top() / face_height

                if(face_left > face_width):
                    if(eye1.left() > (face_right - eye1.right())):
                        # eye1は右目
                        face_rect_dict['eye_to_side'] = (face_right - eye1.right()) / face_width
                    else:
                        # eye1は左目
                        face_rect_dict['eye_to_side'] = eye1.left() / face_width

            # 両目検出時
            if eye_count == 2:
                eye2 = eyes[1]
                eye_to_eye = eye1.left() - eye2.right()
                face_rect_dict['eye_to_eye'] = eye_to_eye / face_width

                face_rect_dict['eye_to_jaw'] = min(eye1.bottom(), eye2.bottom()) / face_height
                face_rect_dict['eye_to_forehead'] = min(eye1.top(), eye2.top()) / face_height

            result[p_file.stem + '_' + str(i)] = copy.deepcopy(face_rect_dict)

        print(face_rect_dict)

    with open(output_path, 'w') as fp:
        json.dump(result, fp)

get_anime_face_ratio()  