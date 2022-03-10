import cv2 as cv

def rescaleFrame(frame,scale = 0.75):
    # Images - Videos - Live Camera
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width,height)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
def changeRes(width,height):
    # Live Camera
    capture.set(3,width)
    capture.set(4,height)

# Video Reading

capture = cv.VideoCapture("D:/Programming/Python_Projects/Computer Vision/Resources/Video/clean.mp4")
# capture = cv.VideoCapture(0)
if not capture.isOpened():
    print("Cannot open camera")
    exit()

# print(capture.get(cv.CAP_PROP_FRAME_WIDTH))
# print(capture.get(cv.CAP_PROP_FRAME_HEIGHT))

while True:
    # Capture frame-by-frame
    isTrue, frame = capture.read()

    # if frame is read correctly ret is True
    if not isTrue:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame_resized = rescaleFrame(frame)
    cv.imshow("clean", frame)
    cv.imshow("resized",frame_resized)

    if cv.waitKey(24) & 0xFF == ord('d'):
        break



capture.release()
cv.destroyAllWindows()

