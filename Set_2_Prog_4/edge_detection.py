# edge_detection.py
import cv2
from img import img   # Import image from img.py

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur before edge detection
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Canny Edge Detection
edges = cv2.Canny(blur, 50, 150)

# Show images
cv2.imshow("Original", img)
cv2.imshow("Gray Image", gray)
cv2.imshow("Edges (Canny)", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()