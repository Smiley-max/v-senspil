import os
import time
import ctypes

ctypes.windll.user32.MessageBoxW(0, "You has been warned.", "WARNING", 0x40 | 0x1)
time.sleep(5)
os.system("shutdown /s /t 0")