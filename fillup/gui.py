import tkinter as tk
from PIL import Image
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytesseract
import pandas as pd

class Gui:
    driver = None
    data = None
    XPATH_TO_SEARCH = None
    XPATH_TO_ITEMS = None

    def open_driver(self):
        if self.driver is None:
            self.driver = webdriver.Chrome()
            self.driver.get('https://google.com')

    def close_driver(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None

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
                # img = img.resize((300, 300))  # Resize for display
                # img_tk = ImageTk.PhotoImage(img)
                # Show in label
                # label.config(image=img_tk)
                # label.image = img_tk  # Keep reference to avoid garbage collection

                text_ext = pytesseract.image_to_string(image=img)
                l2.config(text=text_ext)
                self.data = text_ext

        # button to open browser
        tk.Button(self.root, text="open browser", command=self.open_driver).pack(pady=20)

        # button to upload image
        button = tk.Button(self.root, text="Upload Image", command=upload_image)
        button.pack()

        # label to display image text
        l2 = tk.Label(self.root)
        l2.pack()

        # button to insert data into browser
        insert_button = tk.Button(self.root, text= "Insert data", command=self.insert_data)
        insert_button.pack()

        # button to close browser
        tk.Button(self.root, text="close browser", command=self.close_driver).pack(pady=20)

        # start the gui
        tk.mainloop()

    def insert_data(self):
        search_bar = self.driver.find_element(By.ID, self.XPATH_TO_SEARCH)

        for row in self.data:
            search_bar.send_keys(row[0])
            items = self.driver.find_elements(By.XPATH, self.XPATH_TO_ITEMS)
            for item in items:
                if item.text == row[1]:
                    item.click()
        