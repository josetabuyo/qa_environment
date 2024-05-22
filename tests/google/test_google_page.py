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
        pass

    driver = False

    
    def tearDown(self):
        # Close the webdriver after all tests have run
        if self.driver:
            self.driver.quit()

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

        # Call the function to create the file
        logger = logging.getLogger(__name__)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        
        logger.info("DEBUG info INFOINFOINFOINFOINFO")
        logger.debug("DEBUG debug INFOINFOINFOINFOINFO")

        logger.log("DEBUG log pelao INFOINFOINFOINFOINFO")
        
        
        file_path = create_file_with_random_word()
        print(f"File created: {file_path}")

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

