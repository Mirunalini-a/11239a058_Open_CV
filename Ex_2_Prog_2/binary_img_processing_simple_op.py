import cv2
import numpy as np
from img import img   # import generated image

# ---- Convert to grayscale ----
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ---- Binary Thresholding ----
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# ---- Structuring Element (Kernel) ----
kernel = np.ones((5, 5), np.uint8)

# ---- Erosion ----
erosion = cv2.erode(binary, kernel, iterations=1)

# ---- Dilation ----
dilation = cv2.dilate(binary, kernel, iterations=1)

# ---- Opening ----
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

# ---- Closing ----
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

# ---- Display ----
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale", gray)
cv2.imshow("Binary Image", binary)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
