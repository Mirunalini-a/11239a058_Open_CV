import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found!")
    exit()

# Define kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
erosion = cv2.erode(img, kernel, iterations=1)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Eroded Image", erosion)

# Save output (optional)
cv2.imwrite("eroded_output.jpg", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()