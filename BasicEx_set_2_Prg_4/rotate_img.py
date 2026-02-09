import cv2
from img import img

angle = 45   # change this to any value you want

if img is None:
    print("Error: Image not available!")
else:
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)

    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img, matrix, (w, h))

    cv2.imshow("Original Image", img)
    cv2.imshow("Rotated Image", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

