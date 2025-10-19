# Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options



class Driver:
    def __init__(self):
        self.driver = None 
        self.options = Options()
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("--headless=new")  # Uncomment if needed

        self.service = Service(ChromeDriverManager().install())

    def open_browser(self):
        if self.driver is None:
            self.driver = webdriver.Chrome(service=self.service, options=self.options)
            self.driver.get('https://google.com')

    def close_browser(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None
    
    def insert_data(self, data=["hello"]):
        self.XPATH_TO_SEARCH = "//textarea[@name='q']"
        self.XPATH_TO_ITEMS = '//*[@id="Alh6id"]/div[1]/div/ul/li'
        search_bar = self.driver.find_element(By.XPATH, self.XPATH_TO_SEARCH)

        for row in data:
            search_bar.clear()
            search_bar.send_keys(row)
            self.driver.implicitly_wait(5)
            items = self.driver.find_elements(By.XPATH, self.XPATH_TO_ITEMS)
            items[0].click()