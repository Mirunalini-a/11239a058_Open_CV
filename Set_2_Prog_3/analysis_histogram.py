# histogram_analysis.py
import cv2
import matplotlib.pyplot as plt
from img import img   # Import image from img.py

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calculate histogram for grayscale image
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# Plot grayscale histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity (0-255)")
plt.ylabel("Number of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()


# -----------------------------
# Color Histogram (Optional)
# -----------------------------

colors = ('b', 'g', 'r')
plt.figure()
plt.title("Color Histogram")
plt.xlabel("Pixel Intensity (0-255)")
plt.ylabel("Number of Pixels")

for i, col in enumerate(colors):
    hist_color = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist_color, color=col)
    plt.xlim([0, 256])

plt.show()