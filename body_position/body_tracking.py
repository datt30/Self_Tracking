import cv2
import mediapipe as mp
import helpers.geometric_operations as geo_hlp
import helpers.draw as draw_hlp

CHIN_POINT = [152]
SHOULDERS_POINTS = [11, 12]
MINIMUM_ERGONOMIC_DISTANCE = 25

mp_holistic = mp.solutions.holistic
holistic = mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)


def check_good_position(chin_point, midbody_point):
    distance = geo_hlp.euclidean_distance(chin_point.get('x'),
                                          chin_point.get('y'),
                                          midbody_point.get('x'),
                                          midbody_point.get('y'))

    return 1 if distance > MINIMUM_ERGONOMIC_DISTANCE else 0


def body_detection(image):
    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to pass by reference.
    image.flags.writeable = False
    results = holistic.process(image)

    # Draw landmark annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image_hight, image_width, _ = image.shape

    if results.face_landmarks and results.pose_landmarks:
        chin_key_point = geo_hlp.get_points_from_landmarks(CHIN_POINT,
                                                           results.face_landmarks.landmark,
                                                           image_width,
                                                           image_hight)

        shoulders_key_points = geo_hlp.get_points_from_landmarks(SHOULDERS_POINTS,
                                                                 results.pose_landmarks.landmark,
                                                                 image_width,
                                                                 image_hight)

        body_midpoint = geo_hlp.get_body_midpoint(shoulders_key_points[0], shoulders_key_points[1])

        points_to_draw = chin_key_point + shoulders_key_points
        points_to_draw.append(body_midpoint)

        image = draw_hlp.draw_key_points(image, points_to_draw)
        position_result = check_good_position(chin_key_point[0], body_midpoint)

    return image, position_result
