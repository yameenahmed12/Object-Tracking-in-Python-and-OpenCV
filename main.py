import cv2
from tracker import *

# Create tracker object
tracker = EuclideanDistTracker()

# Object detection from Stable camera, current frame and background model being subtracted and refined
cap = cv2.VideoCapture("traffic.mp4")
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40, detectShadows= True)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

while True:
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if not ret:
        print("Failed to grab frame, video may have ended or failed to load.")
        break

    roi = frame[340:720, 500:800]

    mask = object_detector.apply(roi)
    mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)[1]
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Correctly find contours and process each one
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 250:
            x, y, w, h = cv2.boundingRect(cnt)
            detections.append([x, y, w, h])

    # Object Tracking
    boxes_ids = tracker.update(detections)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        cv2.putText(roi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("roi", roi)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(30)
    if key == 27:  # ESC key to break
        break

cap.release()
cv2.destroyAllWindows()
