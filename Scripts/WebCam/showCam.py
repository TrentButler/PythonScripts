import cv2

cv2.namedWindow("aWindow")

videoCapture = cv2.VideoCapture(0) #FIRST ENABLED WEBCAM?

if videoCapture.isOpened():
    captureOn, frame = videoCapture.read() # GET THE FRAME OF THE WEBCAM

else:
    captureOn = False

while captureOn:
    cv2.imshow("aWindow", frame)
    captureOn, frame = videoCapture.read()

    keyPress = cv2.waitKey(20)
    if keyPress == 27: #ESCAPE KEY
        break

cv2.destroyWindow("aWindow")
videoCapture.release()

