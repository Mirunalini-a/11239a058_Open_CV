import cv2

# Read the image
img = cv2.imread("img.png")

# Check if image is loaded
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("HSV Image", hsv)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
