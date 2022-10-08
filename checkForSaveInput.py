import cv2

def checkForSaveInput(image, key):
    if key == ord('s'):
        savePhoto(image)

def savePhoto(image):
    cv2.imwrite(filename='saved_img.jpg', img=image)

    print("Processing image...")
    img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
    print("Converting RGB image to grayscale...")
    gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
    print("Converted RGB image to grayscale...")
    print("Resizing image to 28x28 scale...")
    img_ = cv2.resize(gray,(28,28))
    print("Resized...")
    img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
    print("Image saved!")
