import unittest
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as Options
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

import nose2
import os
import sys

#  Add project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from libs.tools import tools
from pom.google import GooglePage
from pom.google.results import ResultsPage


class test_google_page(unittest.TestCase):

    def setUp(self):
        pass

    driver = False

    
    def tearDown(self):
        # Close the webdriver after all tests have run
        if self.driver:
            self.driver.quit()

    def test_not_web_scrapping_example(self):
        """ Dummy test to show that the tests are running"""

        self.assertIsNotNone(True)

    def test_search_for_terms(self):
        """ Test that a search for "python" returns results """
        driver = tools.set_driver()

        google = GooglePage(driver)
        google.reach()
        
        google.search("python")
        
        results = ResultsPage(driver)
        
        result_stats =  results.get_result_stats()

        self.assertIsNotNone(result_stats)
        
        return    

if __name__ == '__main__':
    
    nose2.main()

