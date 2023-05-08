import cv2
import numpy as np

# Create a blank image
image = np.zeros((300, 512, 3), np.uint8)

# Create a window to display the image
cv2.namedWindow('image')
cv2.resizeWindow('image', 300, 300)

# Create a function to update the image based on trackbar values
def update_image(hue, saturation, value):
    # Set the hue, saturation, and value values for the image
    image[:] = [hue, saturation, value]

    # Convert the image from HSV to BGR for display purposes
    bgr_image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)

    # Show the updated image
    cv2.imshow('image', bgr_image)

# Create trackbars for adjusting the hue, saturation, and value values
cv2.createTrackbar('Hue', 'image', 0, 179, lambda x: update_image(x, cv2.getTrackbarPos('Saturation', 'image'), cv2.getTrackbarPos('Value', 'image')))
cv2.createTrackbar('Saturation', 'image', 0, 255, lambda x: update_image(cv2.getTrackbarPos('Hue', 'image'), x, cv2.getTrackbarPos('Value', 'image')))
cv2.createTrackbar('Value', 'image', 0, 255, lambda x: update_image(cv2.getTrackbarPos('Hue', 'image'), cv2.getTrackbarPos('Saturation', 'image'), x))

# Set the initial trackbar values
cv2.setTrackbarPos('Hue', 'image', 0)
cv2.setTrackbarPos('Saturation', 'image', 0)
cv2.setTrackbarPos('Value', 'image', 0)

# Show the initial image
update_image(0, 0, 0)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
