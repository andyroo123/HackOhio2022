from concurrent.futures import process
import subprocess
import os
from matplotlib.backend_bases import key_press_handler
import pyautogui
import time
import signal
from checkForQuitInput import quitProgram

pro = 89

def killNotePad():
    os.kill(pro.pid, signal.SIGTERM)

def startNotePad(text,end):
    path = r'text.txt'
    global pro

    pro = subprocess.Popen(['notepad.exe'])
    time.sleep(3)
    while(end == False):
        pyautogui.write(text, interval = 0.1)
