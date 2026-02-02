import cv2

# Read the image
img = cv2.imread("img.png")

# Check if image is loaded
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Grayscale Image", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
