import subprocess
import os
from matplotlib.backend_bases import key_press_handler
import pyautogui
import time


path = r'text.txt'


subprocess.Popen(['notepad.exe'])
time.sleep(3)
pyautogui.write('Hello There', interval = 0.1)
pyautogui.press('enter')
pyautogui.write('How is the Weather?', interval = 0.1)
pyautogui.press('enter')



