import cv2
import report
import threading
from statistics import mode
from blink import blink_tracking
from body_position import body_tracking

result_inspector_thread = None

# blink variables
blinks_per_minute = []
eye_blink_signal = []
blink_counter = 0
previous_ratio = 100

# body position variables
body_position_per_minute = []
body_position_counter_list = []


def result_inspector():
    global blink_counter, body_position_counter_list, result_inspector_thread
    result_inspector_thread = threading.Timer(60.0, result_inspector)
    result_inspector_thread.start()

    if blink_counter > 0:
        blinks_per_minute.append(blink_counter)
        blink_counter = 0

    if body_position_counter_list:
        body_position_per_minute.append(mode(body_position_counter_list))


result_inspector()

# init tracking resources
cap = cv2.VideoCapture(0)

while True:
    # Esc key exit action
    if cv2.waitKey(5) & 0xFF == 27:
        break

    success, image = cap.read()
    if not success:
        break

    image, blink_counter, eye_blink_signal, previous_ratio = blink_tracking.blink_detection(image,
                                                                                            blink_counter,
                                                                                            eye_blink_signal,
                                                                                            previous_ratio)

    image, position_result = body_tracking.body_detection(image)
    body_position_counter_list.append(position_result)

    # show the output image
    cv2.putText(image, f'Blinks: {blink_counter}', (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Tracking Blink", image)


report.generate_report(blinks_per_minute, body_position_per_minute)
report.show_last_report()

cap.release()
cv2.destroyAllWindows()
result_inspector_thread.cancel()
