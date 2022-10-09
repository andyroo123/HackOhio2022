import cv2

def checkForQuitInput(webcam, key):
    if key == ord('q'):
        quitProgram()
        webcam.release()
        return True
    return False

def quitProgram():
    print("Turning off camera.")
    print("Camera off.")
    print("Program ended.")
    cv2.destroyAllWindows()

