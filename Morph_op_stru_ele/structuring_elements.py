import cv2

# Read image
img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found!")
    exit()

# Create different kernels
kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
kernel_cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (7, 7))

# Apply erosion with each kernel
rect = cv2.erode(img, kernel_rect)
ellipse = cv2.erode(img, kernel_ellipse)
cross = cv2.erode(img, kernel_cross)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Rectangular Kernel", rect)
cv2.imshow("Elliptical Kernel", ellipse)
cv2.imshow("Cross Kernel", cross)

# Save outputs (optional)
cv2.imwrite("rect_output.jpg", rect)
cv2.imwrite("ellipse_output.jpg", ellipse)
cv2.imwrite("cross_output.jpg", cross)

cv2.waitKey(0)
cv2.destroyAllWindows()