import cv2
from img import img   # Import generated image

# Resize image
resized = cv2.resize(img, (400, 300))

# Convert to grayscale
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Edge Detection using Canny
edges = cv2.Canny(blur, 100, 200)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", resized)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Blurred Image", blur)
cv2.imshow("Edge Detection", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
