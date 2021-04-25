import cv2


def draw_eye_lines(image, left_point, right_point, center_top, center_bottom):
    cv2.line(image, (left_point[0], left_point[1]), (right_point[0], right_point[1]), (255, 0, 0), 2)
    cv2.line(image, (center_top[0], center_top[1]), (center_bottom[0], center_bottom[1]), (255, 0, 0), 2)
    return image


def draw_key_points(image, key_points):
    for point in key_points:
        image = cv2.circle(image, (int(point['x']), int(point['y'])), radius=2, color=(0, 0, 255), thickness=-1)
    return image
