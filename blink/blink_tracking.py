import cv2
import dlib
from blink.helpers import get_EAR

# Initializing the face detector and facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("blink/models/shape_predictor_68_face_landmarks.dat")


def draw_eye_lines(frame, left_point, right_point, center_top, center_bottom):
    cv2.line(frame, (left_point[0], left_point[1]), (right_point[0], right_point[1]), (255, 0, 0), 2)
    cv2.line(frame, (center_top[0], center_top[1]), (center_bottom[0], center_bottom[1]), (255, 0, 0), 2)


def blink_detection(frame, blink_counter, eye_blink_signal, previous_ratio):
    # Converting a color frame into a grayscale frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Creating an object in which we will sore detected faces
    faces = detector(gray)
    for face in faces:
        # Creating an object in which we will sore detected facial landmarks
        landmarks = predictor(gray, face)

        # Calculating left eye aspect ratio
        left_eye_ratio, left_point, right_point, center_top, center_bottom = get_EAR([36, 37, 38, 39, 40, 41],
                                                                                     landmarks)
        draw_eye_lines(frame, left_point, right_point, center_top, center_bottom)

        # Calculating right eye aspect ratio
        right_eye_ratio, left_point, right_point, center_top, center_bottom = get_EAR([42, 43, 44, 45, 46, 47],
                                                                                      landmarks)
        draw_eye_lines(frame, left_point, right_point, center_top, center_bottom)

        # Calculating aspect ratio for both eyes
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2

        # Appending blinking ratio to a list eye_blink_signal
        eye_blink_signal.append(blinking_ratio)
        if blinking_ratio < 0.20 < previous_ratio:
            blink_counter = blink_counter + 1

        previous_ratio = blinking_ratio

    return frame, blink_counter, eye_blink_signal, previous_ratio
