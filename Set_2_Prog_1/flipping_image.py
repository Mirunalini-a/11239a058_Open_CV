# flip_image.py
import cv2
from img import img   # Import image from img.py

# Flip codes:
# 0  = vertical flip
# 1  = horizontal flip
# -1 = both flips

flip_vertical = cv2.flip(img, 0)
flip_horizontal = cv2.flip(img, 1)
flip_both = cv2.flip(img, -1)

# Show images
cv2.imshow("Original", img)
cv2.imshow("Vertical Flip", flip_vertical)
cv2.imshow("Horizontal Flip", flip_horizontal)
cv2.imshow("Both Flip", flip_both)

cv2.waitKey(0)
cv2.destroyAllWindows()