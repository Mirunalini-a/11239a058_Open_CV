import cv2
import numpy as np

# Create a simple image (blue background)
img = np.zeros((300, 400, 3), dtype=np.uint8)
img[:] = (255, 0, 0)  # Blue color (BGR)

cv2.putText(img, "Hello OpenCV", (50, 150),
            cv2.FONT_HERSHEY_SIMPLEX, 1,
            (255, 255, 255), 2)

cv2.imwrite("img.png", img)
