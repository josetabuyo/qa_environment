from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
import configparser
import os, json


class Tools:
    _instance = None

    def __init__(self):
        self.configs = {}
        self.read_config_file()

    def read_config_file(self):
        # static contructor begin
        with open(os.path.dirname(__file__) + os.sep + "config.json", encoding='utf-8') as config_file:
            self.config = json.load(config_file)
        
    @staticmethod
    def get_instance():
        if Tools._instance is None:
            Tools._instance = Tools()
        return Tools._instance

    
    def set_driver(self):

        # chrome options
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-setuid-sandbox")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors=yes')
        chrome_options.add_argument('--allow-insecure-localhost')
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--test-type")
        
        
        service_log_path = "chromedriver.log"
        service_args = ['--verbose']
        
        current_dir = os.getcwd()
        
        chrome_path = ""
        chromedriver_path = ""
        
        
        if "app" in current_dir:
            # Docker folder working
            chrome_path = self.config['chrome_path_docker']
            chromedriver_path = self.config['chromedriver_path_docker']
            chrome_options.add_argument("--headless=new")
        else:
            # Local folder working
            chrome_path = self.config['chrome_path_local']
            chromedriver_path = self.config['chromedriver_path_local']
        
        chrome_options.binary_location = chrome_path

        driver = EnrichedDriver(
            service = Service(chromedriver_path, log_path = service_log_path),
            options = chrome_options
        )
        
        return driver

tools = Tools.get_instance()


class EnrichedDriver(webdriver.Chrome):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def find(self, by, locator):
        return WebDriverWait(self, 10).until(EC.presence_of_element_located((by, locator)))
