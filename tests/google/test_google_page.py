import unittest
import logging
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
import allure

#  Add project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from libs.tools import tools
from pom.google import GooglePage
from pom.google.results import ResultsPage

import random
import string


class test_google_page(unittest.TestCase):

    def setUp(self):
        
        log_filename = 'output/'+__name__+'.log'

        # Remove the log file if it exists
        if os.path.exists(log_filename):
            os.remove(log_filename)

        logging.basicConfig(
            format='%(asctime)s - %(levelname)s - %(name)s - %(filename)s - %(funcName)s - %(lineno)d:  %(message)s',
            level=logging.NOTSET,
            filename=log_filename,
            force=True
        )

        self.logger = logging.getLogger(__name__)
    

    driver = False

    
    def tearDown(self):
        # Close the webdriver after all tests have run
        if self.driver:
            self.driver.quit()

    

    @allure.title("Test Authentication")
    @allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
    @allure.tag("NewUI", "Essentials", "Authentication")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "John Doe")
    @allure.link("https://dev.example.com/", name="Website")
    @allure.issue("AUTH-123")
    @allure.testcase("TMS-456")
    def test_not_web_scrapping_example(self):
        """ Dummy test to show that the tests are running"""
        def create_file_with_random_word():
            # Generate a random word
            random_word = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
            
            # Get the root path of the project
            project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
            
            # Create the file path
            file_path = os.path.join(project_root, 'output/random_word.txt')
            
            # Write the random word to the file
            with open(file_path, 'w') as file:
                file.write(random_word)
            
            return file_path

        self.logger.debug("debug DEBUG")
        self.logger.info("info DEBUG")
        self.logger.warning("warning DEBUG")
        self.logger.error("error DEBUG")
        
        
        file_path = create_file_with_random_word()
        print(f"File created: {file_path}")

        self.assertIsNotNone(file_path != "", "File created")
        
        return

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

