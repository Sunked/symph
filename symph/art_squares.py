import os
if os.path.dirname(__file__).startswith("/usr/lib/python3/dist-packages/"):
    from .utils import *
else:
    from utils import *

def settings_art_squares(x, y, path):
    screen = curses.initscr()
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if terminal_size[0] < img.shape[1]:
        img = cv2.resize(img, (terminal_size[0], img.shape[1]))
    if terminal_size[1] < img.shape[0]:
        img = cv2.resize(img, (img.shape[1], terminal_size[1]-1))
    img = cv2.resize(img, (img.shape[1]-x, img.shape[0]-y))
    
    return img, screen

def main_art_squares(void, x, y, path):
    img, screen = settings_art_squares(x, y, path)
    y = 0
    while y < img.shape[0]:
        for x in range(img.shape[1]):
            if img[y, x] >= 0 and img[y, x] <= 100:
                screen.addch(y, x, "░")
                screen.refresh()
            if img[y, x] > 100 and img[y, x] <= 150:
                screen.addch(y, x, "▒")
                screen.refresh()
            if img[y, x] > 150 and img[y, x] <= 200:
                screen.addch(y, x, "▓")
                screen.refresh()
            if img[y, x] > 200:
                screen.addch(y, x, "▇")
                screen.refresh()

        y += 1
    screen.getch()