import cv2 as cv
# Image Reading

# img = cv.imread("D:/Programming/Python_Projects/Computer Vision/Resources/Image/messi.png")
#
# cv.imshow("GOAT", img)
# cv.waitKey(0)

# Image Write
# # k = cv.waitKey(0)
#
# # if k == ord("s"):
# #     cv.imwrite("starry_night.png", img)

# Video Reading

# # capture = cv.VideoCapture("D:/Programming/Python_Projects/Computer Vision/Resources/Video/clean.mp4")
# capture = cv.VideoCapture(0)
# if not capture.isOpened():
#     print("Cannot open camera")
#     exit()
#
# # print(capture.get(cv.CAP_PROP_FRAME_WIDTH))
# # print(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
#
# while True:
#     # Capture frame-by-frame
#     isTrue, frame = capture.read()
#
#     # if frame is read correctly ret is True
#     if not isTrue:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#
#     cv.imshow("clean", frame)
#
#     if cv.waitKey(24) & 0xFF == ord('d'):
#         break
#
#     # # Our operations on the frame come here
#     # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     # # Display the resulting frame
#     # cv.imshow('frame', gray)
#     # if cv.waitKey(20) == ord('q'):
#     #     break
#
# capture.release()
# cv.destroyAllWindows()

# Video Write

# cap = cv.VideoCapture(0)
# # Define the codec and create VideoWriter object
# fourcc = cv.VideoWriter_fourcc(*'DIVX')
# out = cv.VideoWriter('D:/Programming/Python_Projects/Computer Vision/Resources/Video/output.avi', fourcc, 20.0, (640,  480))
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     frame = cv.flip(frame, 1)
#     # write the flipped frame
#     out.write(frame)
#     cv.imshow('frame', frame)
#     if cv.waitKey(1) == ord('q'):
#         break
# # Release everything if job is finished
# cap.release()
# out.release()
# cv.destroyAllWindows()



