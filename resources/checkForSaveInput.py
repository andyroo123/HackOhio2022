import cv2
from moveFile import moveFile
from uploadImages import uploadSavedImg
from useModel import useModel
import os
import shutil

index = 1

def checkForSaveInput(image, key):
    if key == ord('s'):
        savePhoto(image)

def savePhoto(image):
    global index
    cv2.imwrite(filename='./photos/saved_img.jpg', img=image)

    print("Processing image...")
    img_ = cv2.imread('./photos/saved_img.jpg', cv2.IMREAD_ANYCOLOR)
    print("Converting RGB image to grayscale...")
    gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
    print("Converted RGB image to grayscale...")
    print("Resizing image to 28x28 scale...")
    img_ = cv2.resize(gray,(28,28))
    print("Resized...")
    img_resized = cv2.imwrite(filename='./photos/saved_img-final.jpg', img=img_)
    print("Image saved!")
    #letter = 'K'
    #shutil.copy(".\photos\saved_img.jpg", ".\photos\databasePhotos\\" + letter)
    #os.rename(".\photos\databasePhotos\\" + letter + "\saved_img.jpg", ".\photos\databasePhotos\\" + letter + "\\" + letter + str(index) + ".jpg")
    #index = index + 1

    moveFile()
    print("Image Moved!")
    #uploadSavedImg()
    # useModel('test-signlanguage-image-bucket', 'images/testImage0.jpg')
    
