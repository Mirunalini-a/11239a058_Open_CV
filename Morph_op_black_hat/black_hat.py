import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found!")
    exit()

# Define kernel
kernel = np.ones((9, 9), np.uint8)

# Apply Black Hat Transformation
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Black Hat (Dark Features)", blackhat)

# Save output (optional)
cv2.imwrite("blackhat_output.jpg", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()