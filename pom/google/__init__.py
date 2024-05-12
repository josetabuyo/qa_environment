from selenium.webdriver.common.by import By

class GooglePage:
    def __init__(self, driver):
        self.driver = driver
    
    def reach(self):
        self.driver.get("https://www.google.com/")

    def search(self, terms):
        
        search_box = self.driver.find(By.NAME, "q")
        search_box.send_keys(terms)
        search_box.submit()
    