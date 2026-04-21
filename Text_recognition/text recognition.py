import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread("img.png")

if img is None:
    print("Image not found")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

text = pytesseract.image_to_string(thresh)
print("Detected Text:")
print(text)

cv2.imshow("Original", img)
cv2.imshow("Processed", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()