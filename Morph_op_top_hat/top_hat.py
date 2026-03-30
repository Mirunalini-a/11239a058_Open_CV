import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found!")
    exit()

# Define kernel (larger kernel works better for Top Hat)
kernel = np.ones((9, 9), np.uint8)

# Apply Top Hat Transformation
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Top Hat (Bright Features)", tophat)

# Save output (optional)
cv2.imwrite("tophat_output.jpg", tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()