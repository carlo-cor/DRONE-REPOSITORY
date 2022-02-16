from djitellopy import tello
import cv2

#   TELLO OBJECT | CONNECT FUNCTION CALL    #
telloObj = tello.Tello()
telloObj.connect()

#   PRINTS OUT BATTERY  #
print(telloObj.get_battery())

#   CAMERA FRAMES AND DISPLAY   #

def cameraStream():
    telloObj.streamon()
    while True:
        image = telloObj.get_frame_read().frame
        image = cv2.resize(image, (360, 240))
        cv2.imshow("IMAGE DISPLAY: ", image)
        cv2.waitKey(1)

cameraStream()