# Tkinter
import tkinter as tk
from PIL import Image
from tkinter import filedialog

from .driver import Driver
# Data extract
import pytesseract
import pandas as pd

class Gui:
    def __init__(self):
        self.browser = Driver()
        self.load_tk()

    def load_tk(self):
        self.root = tk.Tk()
        self.root.title("Image Input Form Filler")
        self.root.geometry("720x1180")
        
        def upload_image():
            # Open file dialog
            file_path = filedialog.askopenfilename(
                filetypes=[
                    ("PNG files", "*.png"),
                    ("JPEG files", "*.jpg"),
                    ("JPEG files", "*.jpeg"),
                ]
            )
            if file_path:
                # Open and resize image
                img = Image.open(file_path)
                text_ext = pytesseract.image_to_string(image=img)
                text_box.delete('1.0', tk.END)
                text_box.insert('1.0', text_ext)
                self.data = text_ext

        # button to open browser
        tk.Button(self.root, text="open browser", command=self.browser.open_browser).pack(pady=20)

        # button to upload image
        button = tk.Button(self.root, text="Upload Image", command=upload_image)
        button.pack()

        # button to insert data into browser
        insert_button = tk.Button(self.root, text= "Insert data", command= lambda: self.browser.insert_data(text_box.get("1.0", tk.END).splitlines()))
        insert_button.pack()

        # button to close browser
        tk.Button(self.root, text="close browser", command=self.browser.close_browser).pack(pady=20)

        text_box = tk.Text(self.root, height=20, width= 100)
        text_box.pack(pady=5)

        # start the gui
        tk.mainloop()


if __name__ == '__main__':
    mygui = Gui()