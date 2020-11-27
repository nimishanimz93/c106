import cv2

def take_snapshot():
    videoCaptureObject = cv2.VideoCapture(0)
    ret,frame =videoCaptureObject.read()
    print(ret)
    cv2.imwrite("newImg.jpg",frame)
    videoCaptureObject.release()

take_snapshot()