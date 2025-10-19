# Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


class Driver:
    def __init__(self):
        self.driver = None 

    def open_browser(self):
        if self.driver is None:
            self.driver = webdriver.Chrome()
            self.driver.get('https://google.com')

    def close_browser(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None
    
    def insert_data(self):
        search_bar = self.driver.find_element(By.ID, self.XPATH_TO_SEARCH)

        for row in self.data:
            search_bar.send_keys(row[0])
            items = self.driver.find_elements(By.XPATH, self.XPATH_TO_ITEMS)
            for item in items:
                if item.text == row[1]:
                    item.click()

