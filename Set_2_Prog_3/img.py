# img.py
import cv2
import numpy as np

# Create a blank black image (400x400)
img = np.zeros((400, 400, 3), dtype=np.uint8)

# Fill background with light blue color
img[:] = (255, 200, 100)   # BGR format

# Draw shapes
cv2.rectangle(img, (50, 50), (350, 200), (0, 255, 0), 3)
cv2.circle(img, (200, 300), 50, (0, 0, 255), -1)

# Add text
cv2.putText(img, "OpenCV", (120, 180),
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (255, 0, 0), 2)
