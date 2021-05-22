import numpy as np
import cv2 as cv
import yaml

fname = "configfile.yaml"

### variables from configfile
with open(fname, "r") as ymlfile:
   configfile = yaml.safe_load(ymlfile)

current_camera_number = configfile['camera_parameters']['camera_number']
current_width = configfile['camera_parameters']['width']
current_height = configfile['camera_parameters']['height']

cap = cv.VideoCapture(current_camera_number)


if not cap.isOpened():
    print("Cannot open camera")
    exit()
    
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    cap.set(3, current_width)
    cap.set(4, current_height)
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
        
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
