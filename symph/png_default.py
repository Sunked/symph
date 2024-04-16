import os
if os.path.dirname(__file__).startswith("/usr/lib/python3/dist-packages/"):
    from .utils import *
else:
    from utils import *

def settings_png_default(x, y, path):
    screen = curses.initscr()
    img = cv2.imread(path)
    if terminal_size[0] < img.shape[1]:
        img = cv2.resize(img, (terminal_size[0], img.shape[1]))
    if terminal_size[1] < img.shape[0]:
        img = cv2.resize(img, (img.shape[1], terminal_size[1]))
    img = cv2.resize(img, (img.shape[1]-x, img.shape[0]-y))
    
    return img, screen

def main_png_default(void, x, y, path, sym):
    img, screen = settings_png_default(x, y, path)
    y = 0
    while y < img.shape[0]:
        for x in range(img.shape[1]):
            if img[y, x, 0] != 0 and img[y, x, 1] != 0 and img[y, x, 2] != 0:
                if img[y, x, 0] != 64 and img[y, x, 1] != 68 and img[y, x, 2] != 68:
                    if sym.lower() == "ascii":
                        screen.addch(y, x, choice(printable))
                        screen.refresh()
                    else:
                        screen.addstr(y, x, choice(sym))
                        screen.refresh()
        y += 1
    screen.getch()