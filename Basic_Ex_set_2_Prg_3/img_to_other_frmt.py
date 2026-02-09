import cv2
from img import img   # import generated image

# Safety check
if img is None:
    print("Error: Image not available!")
else:
    cv2.imwrite("output.jpg", img)
    cv2.imwrite("output.png", img)
    cv2.imwrite("output.bmp", img)
    cv2.imwrite("output.tif", img)

    print("Image converted and saved as:")
    print("output.jpg, output.png, output.bmp, output.tif")
