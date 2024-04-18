from platform import platform
import os
import argparse

try:
    import yaml
except(ImportError, ModuleNotFoundError):
    print("ERROR: install the pyyaml package on the system: 'pip install pyyaml'")

if os.path.dirname(__file__).startswith("/usr/lib/python3/dist-packages/"):
    from .art_squares import *
    from .png_default import *
    from .png_squares import *
else:
    from art_squares import *
    from png_default import *
    from png_squares import *

def doc_help():
    if platform() == "Windows":
        path = r".\data\setup.yaml"
    else:
        path = r"./data/setup.yaml"
    
    with open(path) as file:
        setup = yaml.safe_load(file)
        version = setup["version"]
        github = setup["github"]
        author = setup["author"]
        name = setup["name"]
        
        helper= f"""
                                                                            
 ░▇▇▇▇▇▇ ░▇▇▇░ ░▇▇▇░ ▇▇▇▇▇░ ░▇▇▇▇▇ ░▇▇▇▇▇▇▇▇  ▇▇▇░ ░▇▇░                     
░▇▇▇▇▇▇▇ ▒▇▇▇░ ▒▇▇▒  ▇▇▇▇▇░ ░▇▇▇▇▇ ▓▇▇▇▇▇▇▇▇░ ▇▇▇░ ░▇▇▒                     
▒▇▇▓      ░▇▇▇░▇▇▓░  ▓▇▇▇▇░ ░▇▇▇▇▇  ▇▇▇  ▇▇▇▒ ▓▇▇░ ░▇▇▒                     
░▇▇▇▇▇▇▇▇  ▇▇▇▇▇▇░  ░▇▇ ▇▇▇ ▇▇ ▇▇▇  ▇▇▇▇▇▇▇▇░ ▓▇▇▇▇▇▇▇▒                     
      ▇▇▇▒   ▇▇▇░   ▇▇▇  ▇▇▇▇▇ ▇▇▇  ▇▇▇       ▓▇▇░ ░▇▇▒                     
░▓▇▇▇▇▇▇▓   ▒▇▇▓░  ▓▇▇▓  ▇▇▇▇  ▇▇▇  ▇▇▇       ▓▇▇░ ░▇▇▒ 


version -> {version}
github -> {github}
author -> {author}



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

--config [CONFIG ...]  configure the program




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



You can use the configuration file (in the directory 'data') to set the default data and not have to constantly enter it.

Read more in README.md

"""
        return helper

def main_msg():
    parser = argparse.ArgumentParser(description="Settings symph", add_help=False)
    parser.add_argument("-h", "--help", action="store_true")
    parser.add_argument("--config",
                        help="configure the program",
                        nargs="+")
    parser.add_argument("photo", help="indicate the path to your photo", nargs="?", default=None)
    parser.add_argument("-s", "--size", 
                        help="indicate the amount of photo cropping", 
                        default=(0, 0), 
                        nargs='+')
    parser.add_argument("-m", "--mode", 
                        help="indicate one of three symbols generation modes (default(0), png_squares(1), art_squares(2))", 
                        default=None)
    parser.add_argument("-sb", "--symbol", 
                        help="specify the generated symbol for the classic mode. You can pass 'ASCII'", 
                        default=None)

    args = parser.parse_args()
    # --help
    if platform() == "Windows":
        pathC = r".\data\config.yaml"
    else:
        pathC = "./data/config.yaml"

    with open(pathC) as fileC:
        conf = yaml.safe_load(fileC)
        if args.help or len(sys.argv) == 1:
            if conf["PATH"] == "None":
                print(doc_help())
                exit()
    # --config
    if args.config:
        with open(pathC, "w") as _fileC:
            try:
                conf[args.config[0].upper()]
            except:
                print("--INCORRECT CONFIGURATION-- enter the correct settings, you can see it in the README.md")
                yaml.safe_dump(conf, _fileC)
                exit()
            try:
                if args.config[0].lower() == "size":
                    conf[args.config[0].upper()]["X"]=args.config[1]
                    conf[args.config[0].upper()]["Y"]=args.config[2]
                    yaml.safe_dump(conf, _fileC)
                else:
                    conf[args.config[0].upper()]=args.config[1]
                    yaml.safe_dump(conf, _fileC)

            except:
                yaml.safe_dump(conf, _fileC)
                print("--AN ERROR HAS OCCURRED--")
                exit()
            
            print("\u001b[1;32mDONE")
            exit()
    
    return args

def generation():
    args = main_msg()
    
    if platform() == "Windows":
        path = r".\data\config.yaml"
    else:
        path = "./data/config.yaml"
    
    with open(path) as file:
        config = yaml.safe_load(file)
        # photo path
        if args.photo is None:
            photo_path = config["PATH"]
        else:
            photo_path = args.photo
        # size
        if args.size == (0, 0):
            if config["SIZE"]["X"] != 0 or config["SIZE"]["Y"] != 0:
                size = (config["SIZE"]["X"], config["SIZE"]["Y"])
            else:
                size = (0, 0)
        else:
            size = args.size
        # mode
        if args.mode is None:
            mode = config["MODE"]
        else:
            mode = args.mode
        
        # symbol
        if args.symbol is None:
            symbol = config["SYMBOL"]
        else:
            symbol = args.symbol
    try:
        if mode.lower() == "default" or str(args.mode) == "0":
            wrapper(main_png_default, int(size[0]), int(size[1]), photo_path, symbol)
        elif mode.lower() == "png_squares" or str(args.mode) == "1":
            wrapper(main_png_squares, int(size[0]), int(size[1]), photo_path)
        elif mode.lower() == "art_squares" or str(args.mode) == "2":
            wrapper(main_art_squares, int(size[0]),int(size[1]), photo_path)
    
    except AttributeError:
        print("ERROR: --INCORRECT FILE PATH OR CONFIGURATION--\nplease, indicate the full path to the photo with its format or write the configuration file correctly")
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