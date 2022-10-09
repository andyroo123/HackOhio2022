# Copies ./photos/saved_img.jpg to testphotos
import shutil


def moveFile():
    shutil.copy("photos\saved_img.jpg", "photos\testPhotos")