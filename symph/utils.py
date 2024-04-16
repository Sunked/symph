import sys
from random import choice
from string import printable
import shutil

try:
    import curses
except (ImportError, ModuleNotFoundError):
    print("ERROR: install the curses package on the system: 'pip install windows-curses'")
    exit()
from curses import wrapper

try:
    import cv2
except (ImportError, ModuleNotFoundError): 
    print("ERROR: install the opencv package on the system: 'pip install opencv-python'")
    exit()

terminal_size = shutil.get_terminal_size()