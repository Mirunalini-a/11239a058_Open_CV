import cv2
from img import img   # import the generated image

# Safety check
if img is None:
    print("Error: Image not available!")
else:
    cv2.imshow("Image Display", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
