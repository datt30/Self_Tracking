import cv2
from threading import Timer
import schedule
from blink import blink_tracking
import report

blinks_per_minute = []
# Creating a list eye_blink_signal
eye_blink_signal = []
# Creating an object blink_counter
blink_counter = 0
previous_ratio = 100


def result_inspector():
    global blink_counter
    print("blinks:")
    print(blink_counter)
    blinks_per_minute.append(blink_counter)
    blink_counter = 0


# init tracking resources
cap = cv2.VideoCapture(0)
result_inspector_schedule = schedule.every(1).minutes.do(result_inspector)
schedule.run_pending()

while True:
    # exit from detection video frames loop
    if cv2.waitKey(2) & 0xFF == ord('e'):  # press e to exit
        break

    ret, frame = cap.read()
    if not ret:
        break

    frame, blink_counter, eye_blink_signal, previous_ratio = blink_tracking.blink_detection(frame,
                                                                                            blink_counter,
                                                                                            eye_blink_signal,
                                                                                            previous_ratio)


    # show the output image
    cv2.putText(frame, f'Blinks: {blink_counter}', (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Tracking Blink", frame)


report.generate_report(blinks_per_minute, None)
report.show_last_report()

cap.release()
cv2.destroyAllWindows()
