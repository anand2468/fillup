import argparse
from fillup.gui import Gui
from fillup.subscription import check_sub

def main():
    parser = argparse.ArgumentParser(description="a command line tool to fill forms automatically with image input")
    args = parser.parse_args()
    
    if check_sub():
        gui = Gui()
        gui.load_tk()
    else:
        print("subscription over contact: 9182377052")

if __name__ == "__main__":
    main()