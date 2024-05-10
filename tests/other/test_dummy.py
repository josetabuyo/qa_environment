import unittest
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as Options
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class test_dummy(unittest.TestCase):

    def setUp(self):
        pass

    driver = False

    def set_driver(self):
        
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument("no-sandbox")
        options.add_argument('--headless')
        options.add_argument("--start-maximized")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--start-maximized")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--remote-debugging-pipe")
        
        # options.add_argument("--test-type")

        
        service_log_path = "chromedriver.log"
        service_args = ['--verbose']


        # options.binary_location = "/usr/local/bin/"

        # Set up the webdriver and navigate to Google.com
        self.driver = webdriver.Chrome(
            executable_path='/usr/local/bin/chromedriver-linux64/chromedriver',
            service_args = service_args,
            service_log_path = service_log_path,
            options = options
        )

        
        self.driver.get("https://www.google.com/")
    
    
    def tearDown(self):
        # Close the webdriver after all tests have run
        if self.driver:
            self.driver.quit()


    def test_not_web_scrapping_example_one(self):
        """ Dummy test to show that the tests are running"""

        self.assertIsNotNone(True)


    def test_not_web_scrapping_example_two(self):
        """ Dummy test to show that the tests are running"""

        self.assertIsNotNone(True)


    def test_not_web_scrapping_example_three(self):
        """ Dummy test to show that the tests are running"""

        self.assertIsNotNone(True)


if __name__ == '__main__':
    import nose2
    nose2.main()

