import cv2
import numpy as np

# Create a black image
img = np.zeros((300, 300), dtype=np.uint8)

# Draw white shapes (foreground)
cv2.rectangle(img, (50, 50), (250, 250), 255, -1)  # filled rectangle
cv2.circle(img, (150, 150), 40, 0, -1)             # black hole inside
cv2.circle(img, (80, 80), 10, 255, -1)             # small noise
cv2.circle(img, (220, 220), 10, 255, -1)           # small noise

# Save image
cv2.imwrite("input.jpg", img)

# Show image
cv2.imshow("Generated Input", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
