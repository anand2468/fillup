import argparse
from fillup.gui import Gui
from fillup.subscription import check_sub
import sys
import shutil


def check_tesseract():
    """Ensure that the Tesseract engine is installed on the system."""
    if not shutil.which("tesseract"):
        sys.stderr.write(
            "Error: Tesseract OCR engine not found.\n"
            "Please install it manually:\n"
            "  - macOS: brew install tesseract\n"
            "  - Ubuntu/Debian: sudo apt-get install tesseract-ocr\n"
            "  - Windows: download from https://github.com/UB-Mannheim/tesseract/wiki\n"
        )
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="a command line tool to fill forms automatically with image input")
    args = parser.parse_args()

    check_tesseract()
    
    if check_sub():
        gui = Gui()
    else:
        print("subscription over contact: 9182377052")

if __name__ == "__main__":
    main()