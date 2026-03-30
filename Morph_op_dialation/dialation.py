import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found!")
    exit()

# Define kernel
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilation = cv2.dilate(img, kernel, iterations=1)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Dilated Image", dilation)

# Save output (optional)
cv2.imwrite("dilated_output.jpg", dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()