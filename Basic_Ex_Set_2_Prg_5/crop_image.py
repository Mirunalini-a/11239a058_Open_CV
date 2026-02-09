import cv2
from img import img   # import generated image

# Safety check
if img is None:
    print("Error: Image not available!")
else:
    print("Image shape (Height, Width, Channels):", img.shape)

    # ---- Crop values (change if you want) ----
    x = 100   # starting column
    y = 100   # starting row
    w = 250   # width
    h = 200   # height

    # Cropping
    cropped = img[y:y+h, x:x+w]

    # Display
    cv2.imshow("Original Image", img)
    cv2.imshow("Cropped Image", cropped)

    # Save
    cv2.imwrite("cropped_output.jpg", cropped)
    print("Cropped image saved as cropped_output.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
