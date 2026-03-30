import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found!")
    exit()

# Define kernel
kernel = np.ones((5, 5), np.uint8)

# Apply Closing (Dilation followed by Erosion)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Closing (Holes Filled)", closing)

# Save output (optional)
cv2.imwrite("closing_output.jpg", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()