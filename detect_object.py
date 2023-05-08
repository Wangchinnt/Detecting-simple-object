import cv2

from ulti import get_limits


yellow = [0, 255, 255] # yellow in BRG color space
green = [0, 255, 0] # green in BRG color space
blue = [255, 0 , 0] # blue in BRG color space
orange = [0, 165, 255] # orange in BRG color space
purple = [127, 0, 127] # purple in BRG color space
# Create a VideoCapture object to capture video from the default camera (0)
cap = cv2.VideoCapture(0)

# Define the kernel for morphological operations
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# Check if the camera was opened successfully
if not cap.isOpened():
    print("Error opening video stream")

# Read the frames from the video stream
while cap.isOpened():
    # Capture each frame
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))

    # Check if the frame was captured successfully
    if not ret:
        print("Error reading video stream")
        break
    
    # Convert the color of frame to HSV format
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Blur the image using Gaussian blur
    blur = cv2.GaussianBlur(hsvImage, (5, 5), 0)
    
    #get limit of yellow color
    lowerLimit, upperLimit = get_limits(color=yellow)
    mask = cv2.inRange(blur, lowerLimit, upperLimit)
        
 
    # Perform morphological opening to remove noise
    mask = cv2.erode(mask, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=2)
    
 
    # Find the contours of the object in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter the contours based on size and aspect ratio
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 1000:
            continue
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
    
        x, y, w, h = cv2.boundingRect(approx)

        cropped = frame[y:y+h+10, x:x+w+10]
        if cropped is not None:
            cv2.imshow("cropped", cropped)     
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)

       
        
    # Display the resulting frame
   
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
