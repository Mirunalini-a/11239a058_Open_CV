import cv2

# Read the image
img = cv2.imread("img.png")

# Check if image is loaded correctly
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Image properties
    height, width, channels = img.shape
    size = img.size
    datatype = img.dtype

    print("Width :", width)
    print("Height :", height)
    print("Channels :", channels)
    print("Image Size :", size)
    print("Data Type :", datatype)
