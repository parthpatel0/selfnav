import cv2
import numpy as np

video = cv2.VideoCapture("ap_road_day.mp4")

while True:#incase file cannot be opened
    ret, orig_frame = video.read()
    if not ret:
        video = cv2.VideoCapture("ap.mp4")
        continue

    frame = cv2.GaussianBlur(orig_frame, (5, 5), 0) #applying blur to smooth edges
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #rgb to grey scale
    #lower = np.array([0, 0, 210])
    #upper = np.array([255, 40 , 255])
    #mask = cv2.inRange(hsv, lower,upper)
    #mask = cv2.inRange(hsv, np.array([0, 210, 0]), np.array([255, 255, 255]))
    edges = cv2.Canny(hsv,90 , 150) #detecting edges using gradiant canny function

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, maxLineGap= 60,) # drawing green lines
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imshow("frame", frame) # display result
    #cv2.imshow("edges", edges)
    #cv2.imshow("mask",hsv)
    key = cv2.waitKey(1)
    if key == 27:
        break
video.release()
cv2.destroyAllWindows()
