import argparse
import os
if os.path.dirname(__file__).startswith("/usr/lib/python3/dist-packages/"):
    from .setup import setup
    from .art_squares import *
    from .png_default import *
    from .png_squares import *
else:
    from setup import setup
    from art_squares import *
    from png_default import *
    from png_squares import *

helper = f"""
                                                                            
 ░▇▇▇▇▇▇ ░▇▇▇░ ░▇▇▇░ ▇▇▇▇▇░ ░▇▇▇▇▇ ░▇▇▇▇▇▇▇▇  ▇▇▇░ ░▇▇░                     
░▇▇▇▇▇▇▇ ▒▇▇▇░ ▒▇▇▒  ▇▇▇▇▇░ ░▇▇▇▇▇ ▓▇▇▇▇▇▇▇▇░ ▇▇▇░ ░▇▇▒                     
▒▇▇▓      ░▇▇▇░▇▇▓░  ▓▇▇▇▇░ ░▇▇▇▇▇  ▇▇▇  ▇▇▇▒ ▓▇▇░ ░▇▇▒                     
░▇▇▇▇▇▇▇▇  ▇▇▇▇▇▇░  ░▇▇ ▇▇▇ ▇▇ ▇▇▇  ▇▇▇▇▇▇▇▇░ ▓▇▇▇▇▇▇▇▒                     
      ▇▇▇▒   ▇▇▇░   ▇▇▇  ▇▇▇▇▇ ▇▇▇  ▇▇▇       ▓▇▇░ ░▇▇▒                     
░▓▇▇▇▇▇▇▓   ▒▇▇▓░  ▓▇▇▓  ▇▇▇▇  ▇▇▇  ▇▇▇       ▓▇▇░ ░▇▇▒ 


version -> {setup["version"]}
github -> {setup["github"]}
author -> {setup["author"]}



usage: main.py [-h] [-s SIZE [SIZE ...]] [-m MODE] [-sb SYMBOL] photo

Settings symph

positional arguments:
photo                 indicate the path to your photo

options:
-h, --help            show this help message and exit

-s [SIZE ...], --size [SIZE ...]
                        indicate the amount of photo cropping (two numbers without commas)

-m, --mode            indicate one of three symbols generation modes
                        (default(0), png_squares(1), art_squares(2))

-sb, --symbol         specify the generated symbol for the classic mode.
                        You can pass 'ASCII'



Use smaller photos. 
It is advisable to use photographs no larger than 800x800. 
When using large volumes of photos, the following may occur: 
an exception about incorrect size, 
severe distortion of the photo, 
non-recognition of the photo and many other problems.
You can use some services to reduce the size of photos. I can recommend IloveIMG

a program that works with PNG images does not recognize black colors and shades of gray (68, 68, 64) RGB. 
I advise you not to use black images for PNG work.

If your photo is not recognized, 
please check the size of your photo and the shades, 
you can also adjust the cut of the photo, try your best.

The program is not entirely stable. 
When generating inscriptions, there can be big problems, 
an example of this is the inscription for this documentation, in which some adjustment was used.

The program on Windows works almost the same, but recognizes photo a little worse.
"""

def main_msg():
    parser = argparse.ArgumentParser(description="Settings symph", add_help=False)
    parser.add_argument("-h", "--help", action="store_true")
    parser.add_argument("photo", help="indicate the path to your photo", nargs="?")
    parser.add_argument("-s", "--size", 
                        help="indicate the amount of photo cropping", 
                        default=(0, 0), 
                        nargs='+')
    parser.add_argument("-m", "--mode", 
                        help="indicate one of three symbols generation modes (default(0), png_squares(1), art_squares(2))", 
                        default="default")
    parser.add_argument("-sb", "--symbol", 
                        help="specify the generated symbol for the classic mode. You can pass 'ASCII'", 
                        default="ascii")

    args = parser.parse_args()
    if args.help or len(sys.argv) == 1:
        print(helper)
        exit()
    
    return args

def generation():
    args = main_msg()
    try:
        if args.mode.lower() == "default" or str(args.mode) == "0":
            wrapper(main_png_default, int(args.size[0]), int(args.size[1]), args.photo, args.symbol)
        elif args.mode.lower() == "png_squares" or str(args.mode) == "1":
            wrapper(main_png_squares, int(args.size[0]), int(args.size[1]), args.photo)
        elif args.mode.lower() == "art_squares" or str(args.mode) == "2":
            wrapper(main_art_squares, int(args.size[0]), int(args.size[1]), args.photo)
    
    except AttributeError:
        print("ERROR: --INCORRECT FILE PATH--\nplease, indicate the full path to the photo with its format")
        sys.exit()

    except IndexError:
        print("ERROR: --INVALID PHOTO SIZE--\nplease, indicate the exact cut along x and y without commas")

    except cv2.error:
        print("ERROR: --INVALID PHOTO SIZE--\nplease, adjust the photo to the size of your console, or change the size of the console itself")
        sys.exit()

def main():
    generation()

if __name__ == "__main__":
    main()