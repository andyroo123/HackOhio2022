import cv2

def checkForQuitInput(webcam, key):
    if key == ord('q'):
        quitProgram(webcam)

def quitProgram(webcam):
    print("Turning off camera.")
    webcam.release()
    print("Camera off.")
    print("Program ended.")
    cv2.destroyAllWindows()
