import cv2

# Read the image
img = cv2.imread("img.png")

# Check if image is loaded
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Add text on the image
    cv2.putText(
        img,
        "OpenCV Lab",
        (50, 50),                     # Bottom-left corner of the text
        cv2.FONT_HERSHEY_SIMPLEX,     # Font type
        1,                            # Font scale
        (0, 255, 0),                  # Text color (Green)
        2                             # Thickness
    )

    # Display image
    cv2.imshow("Image with Text", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
