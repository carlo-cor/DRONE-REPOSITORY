import cv2
import numpy as np
import numpy as npObj

width = 640
height = 480
window = cv2.VideoCapture(0)
window.set(3, width)
window.set(4, height)

def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
cv2.createTrackbar("HUE MIN TRACKBAR", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE MAX TRACKBAR", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT MIN TRACKBAR", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT MAX TRACKBAR", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE MIN TRACKBAR", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE MAX TRACKBAR", "HSV", 255, 255, empty)

while True:
    _, img = window.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HUE MIN TRACKBAR", "HSV")
    h_max = cv2.getTrackbarPos("HUE MAX TRACKBAR", "HSV")
    s_min = cv2.getTrackbarPos("SAT MIN TRACKBAR", "HSV")
    s_max = cv2.getTrackbarPos("SAT MAX TRACKBAR", "HSV")
    v_min = cv2.getTrackbarPos("VALUE MIN TRACKBAR", "HSV")
    v_max = cv2.getTrackbarPos("VALUE MAX TRACKBAR", "HSV")
    print(h_min)

    minimums = np.array([h_min, s_min, v_min])
    maximums = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, minimums, maximums)
    result = cv2.bitwise_and(img, img, mask = mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    horizontalStck = np.hstack([img, mask, result])

    # cv2.imshow("ORIGINAL", img)
    # cv2.imshow("HSV COLOR SPACE", imgHSV)
    # cv2.imshow("MASK", mask)
    # cv2.imshow("RESULTS", result)
    cv2.imshow("HORIZONTAL STACK", horizontalStck)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break