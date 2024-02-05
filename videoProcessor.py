import cv2
import numpy as np
from baseTranslator import translate
# Video Path
video_path = 'E:\DIM\images\SOS morse code.mp4'

#Read Video
cap = cv2.VideoCapture(video_path)

#Check Opened sucsessfuly
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Define parameters for light detection
light_threshold = 66  # Adjust this threshold according to your video
light_detected = False
light_start_frame = None
light_end_frame = None
frame_count = 0
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
left_crop = 150  # Number of pixels to crop from the left
right_crop = 70  # Number of pixels to crop from the right
top_crop = 50  # Number of pixels to crop from the top
bottom_crop = 70  # Number of pixels to crop from the bottom
morse = ""
c1 = 0
c2 = 0

while cap.isOpened():
    ret, frame = cap.read()

    # Check if the frame was read successfully\
    if not ret:
        break
    


    # Convert the frame to grayscale for simplicity
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = gray_frame[top_crop:frame_height-bottom_crop, left_crop:frame_width-right_crop]
    #cv2.imshow("frame",gray_frame)
    #cv2.waitKey(0)
    #frame_count += 1
    #print(frame_count)
    


    # Check if there are any light sources in the frame
    light_level = np.mean(gray_frame)
    #print(light_level)
    if light_level > light_threshold and not light_detected:
        light_detected = True
        light_start_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
    elif light_level <= light_threshold and light_detected:
        light_detected = False
        light_end_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
        # Calculate the duration of light in frames
        light_duration = int(light_end_frame - light_start_frame)
        # Convert the frame count to time (assuming 30 frames per second)
        light_duration_seconds = light_duration / 30.0
        print(f"Light detected from frame {light_start_frame} to {light_end_frame} (Duration: {light_duration_seconds} seconds)")
        if light_duration_seconds > 0.3:
            morse = morse + '-'
            c1 += 1
            if c1 == 3:
                c1 = 0
                morse = morse + " "
        else:
            morse = morse + '.'
            c2 += 1
            if c2 == 3:
                c2 = 0
                morse = morse + " "

print(morse)
print(translate(morse))
# Release the video capture object and close all windows
cap.release()
