import numpy as np


# Defining the mid-point
def midpoint(p1, p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)


# Defining the Euclidean distance
def euclidean_distance(left_x, left_y, right_x, right_y):
    return np.sqrt((left_x - right_x)**2 + (left_y - right_y)**2)


# Defining the eye aspect ratio
def get_EAR(eye_points, facial_landmarks):
    # Left point of the eye position [x,y]
    left_point = [facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y]
    # Right point of the eye position [x,y]
    right_point = [facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y]
    # Top mid-point of the eye position [x,y]
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    # Bottom mid-point of the eye position [x,y]
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

    # Calculating length of the horizontal and vertical line
    hor_line_lenght = euclidean_distance(left_point[0], left_point[1], right_point[0], right_point[1])
    ver_line_lenght = euclidean_distance(center_top[0], center_top[1], center_bottom[0], center_bottom[1])
    eye_aspect_ratio = ver_line_lenght / hor_line_lenght

    return eye_aspect_ratio, left_point, right_point, center_top, center_bottom


# extract the x and y coordinates of each point from landmarks in relation to the height and width of the image
def get_points_from_landmarks(points_to_extract, landmarks, image_width, image_hight):
    key_points = []
    for index, landmark in enumerate(landmarks):
        landmark.x
        if index in points_to_extract:
            x_coordinate = landmark.x * image_width
            y_coordinate = landmark.y * image_hight
            key_points.append({
                'x': x_coordinate,
                'y': y_coordinate,
            })
    return key_points


def get_body_midpoint(p1, p2):
    x = int((p1.get('x') + p2.get('x'))/2)
    y = int((p1.get('y') + p2.get('y'))/2)
    return {'x': x, 'y': y}
