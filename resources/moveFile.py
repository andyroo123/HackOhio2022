# Copies ./photos/saved_img.jpg to testphotos
import shutil


def moveFile():
    shutil.copy(".\photos\saved_img.jpg", ".\photos\\testPhotos")
    print("File Copied")

def main():
    moveFile()
    print("main")

if __name__ == "__main__":
    main()
