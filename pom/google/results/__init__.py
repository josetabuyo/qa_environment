from selenium.webdriver.common.by import By

class ResultsPage:
    def __init__(self, driver):
        self.driver = driver
    
    def get_result_stats(self):
        return self.driver.find_element(By.ID, "result-stats")
