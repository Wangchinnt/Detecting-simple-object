# This is a tool that u can use to get color code of an object (HSV color code, RGB color code)
# Step1: Run the file
# Step2: Move the color u want to get color code to the dot on the screen
# Step3: Click left mouse button to get color code
# Result: Color code will be displayed in CMD


import cv2
import numpy as np

# Create a method to get the pixel color at a specific location in the image
def get_pixel_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel_color = hsv_frame[y, x]
        pixel_color_rgb = rgb_frame[y, x]
        print("HSV color code", pixel_color)
        print("RGB color code",pixel_color_rgb)

# Open the video capture device
cap = cv2.VideoCapture(0)

# Create a window to display the video stream
cv2.namedWindow('frame')

# Set the mouse callback function to get the pixel color
cv2.setMouseCallback('frame', get_pixel_color)

while True:
    # Read a frame from the video capture device
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    if not ret:
        break

    # Convert the frame from BGR to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get the center pixel of the frame
    height, width, channels = frame.shape
    cx, cy = int(width/2), int(height/2)

    # Get the color value of the center pixel
    pixel_color = hsv_frame[cy, cx]
    pixel_color_rgb = rgb_frame[cy,cx]

    # Display the original frame with a circle marking the center point
    cv2.circle(frame, (cx, cy), 2, (0, 0, 255), -1)
    cv2.imshow('frame', frame)

    # Wait for a key press and then exit if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture device and close all windows
cap.release()
cv2.destroyAllWindows()
