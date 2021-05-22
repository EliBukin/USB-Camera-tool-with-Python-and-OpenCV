#!/usr/bin/python3

import numpy as np
import cv2
import time
import os
import sys
import yaml

fname = "configfile.yaml"

### variables from configfile
with open(fname, "r") as ymlfile:
   configfile = yaml.safe_load(ymlfile)

current_interval = configfile['config']['interval']
current_fps = configfile['camera_parameters']['fps']
current_camera_number = configfile['camera_parameters']['camera_number']
current_width = configfile['camera_parameters']['width']
current_height = configfile['camera_parameters']['height']
current_dest_folder = configfile['path_vars']['dest_folder']


fps = current_fps
#width = 1280
#height = 720
video_codec = cv2.VideoWriter_fourcc("D", "I", "V", "X")

dest_file = current_dest_folder
interval = current_interval
today = time.strftime("%a-%d.%m.%Y-%H-%M-%S")

cap = cv2.VideoCapture(current_camera_number)
ret = cap.set(3, current_width)
ret = cap.set(4, current_height)

start = time.time()
video_file_count = 1
video_file = os.path.join(dest_file, today + ".avi")
#print("Capture video saved location : {}".format(video_file))

# Create a video write before entering the loop
video_writer = cv2.VideoWriter(
    video_file, video_codec, fps, (int(cap.get(3)), int(cap.get(4)))
)

while cap.isOpened():
    today = time.strftime("%a-%d.%m.%Y-%H-%M-%S")
    start_time = time.time()
    ret, frame = cap.read()
    if ret == True:
#        cv2.imshow("frame", frame)
        if time.time() - start > interval:
            start = time.time()
            video_file_count += 1
            video_file = os.path.join(dest_file, today + ".avi")
            video_writer = cv2.VideoWriter(
                video_file, video_codec, fps, (int(cap.get(3)), int(cap.get(4)))
            )
            # No sleeping! We don't want to sleep, we want to write
            # time.sleep(10)

        # Write the frame to the current video writer
        video_writer.write(frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
