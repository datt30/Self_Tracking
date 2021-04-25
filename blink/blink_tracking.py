import cv2
import dlib
from helpers.geometric_operations import get_EAR
import helpers.draw as draw_hlp

RIGHT_EYE_POINTS = [42, 43, 44, 45, 46, 47]
LEFT_EYE_POINTS = [36, 37, 38, 39, 40, 41]

# Initializing the face detector and facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("blink/models/shape_predictor_68_face_landmarks.dat")


def blink_detection(frame, blink_counter, eye_blink_signal, previous_ratio):
    # Converting a color frame into a grayscale frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Creating an object in which we will sore detected faces
    faces = detector(gray)
    for face in faces:
        # Creating an object in which we will sore detected facial landmarks
        landmarks = predictor(gray, face)

        # Calculating left eye aspect ratio
        left_eye_ratio, left_point, right_point, center_top, center_bottom = get_EAR(LEFT_EYE_POINTS, landmarks)
        draw_hlp.draw_eye_lines(frame, left_point, right_point, center_top, center_bottom)

        # Calculating right eye aspect ratio
        right_eye_ratio, left_point, right_point, center_top, center_bottom = get_EAR(RIGHT_EYE_POINTS, landmarks)
        draw_hlp.draw_eye_lines(frame, left_point, right_point, center_top, center_bottom)

        # Calculating aspect ratio for both eyes
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2

        # Appending blinking ratio to a list eye_blink_signal
        eye_blink_signal.append(blinking_ratio)
        if blinking_ratio < 0.20 < previous_ratio:
            blink_counter += 1

        previous_ratio = blinking_ratio

    return frame, blink_counter, eye_blink_signal, previous_ratio
