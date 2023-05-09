import cv2
from ulti import get_limits
import tkinter as tk
from tkinter import messagebox

color_map = {
    "yellow": [0, 255, 255],
    "green": [0, 255, 0],
    "blue": [255, 0, 0],
    "orange": [0, 165, 255],
    "purple": [127, 0, 127]
}

###################################
# User select color
def select_color():
    color_choice = color_var.get()
    if color_choice not in ['yellow', 'green', 'blue', 'orange', 'purple']:
        messagebox.showerror("Error", "Invalid color choice!")
        return
    root.destroy()

#Initiate window
root = tk.Tk()
root.geometry("400x350")
root.title("Select color")

color_var = tk.StringVar(value="yellow")
color_frame = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10)
color_frame.pack()


tk.Label(color_frame, text="Select color:").pack()

options_frame = tk.Frame(color_frame)
options_frame.pack()

yellow_button = tk.Radiobutton(color_frame, text="Yellow", variable=color_var, value="yellow",
                               fg="black", bg="#F7DC6F", font=("Arial", 12))
green_button = tk.Radiobutton(color_frame, text="Green", variable=color_var, value="green",
                              fg="black", bg="#2ECC71", font=("Arial", 12))
blue_button = tk.Radiobutton(color_frame, text="Blue", variable=color_var, value="blue",
                             fg="black", bg="#3498DB", font=("Arial", 12))
orange_button = tk.Radiobutton(color_frame, text="Orange", variable=color_var, value="orange",
                               fg="black", bg="#F39C12", font=("Arial", 12))
purple_button = tk.Radiobutton(color_frame, text="Purple", variable=color_var, value="purple",
                               fg="black", bg="#9B59B6", font=("Arial", 12))

yellow_button.pack(anchor="w", pady=5)
green_button.pack(anchor="w", pady=5)
blue_button.pack(anchor="w", pady=5)
orange_button.pack(anchor="w", pady=5)
purple_button.pack(anchor="w", pady=5)

select_button = tk.Button(root, text="Select", command=select_color, pady=10)
select_button.pack()

root.mainloop()
####################################


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

    # get limit of yellow color
    lowerLimit, upperLimit = get_limits(color=color_map[color_var.get()])
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

        cropped = frame[y:y + h + 10, x:x + w + 10]
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
