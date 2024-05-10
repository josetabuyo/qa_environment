import os, sys
# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from libs.auditor.Auditor import log, audit
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options as Options
# from webdriver_manager.chrome import ChromeDriverManager

import json

import os

class RpaJobs():


    import os

    def __init__(self):
        """ """

        
    # def create_web_driver(self):
    #     options = Options()
    #     options.add_argument('--headless')
    #     options.add_argument('--no-sandbox')
    #     options.add_argument("--start-maximized")
    #     options.add_argument("--disable-setuid-sandbox")
    #     options.add_argument('--disable-dev-shm-usage')
    #     options.add_argument('--ignore-ssl-errors=yes')
    #     options.add_argument('--ignore-certificate-errors')

    #     service_log_path = "chromedriver.log"
    #     service_args = ['--verbose']

    #     # Set up the webdriver and navigate to Google.com
    #     driver = webdriver.Chrome(
    #         service=ChromeService(ChromeDriverManager().install()),
    #         service_args = service_args,
    #         service_log_path = service_log_path,
    #         options = options
    #     )



    #     return driver
    
    def rpa_get_coupons_from_seg_api(self):
        """ call to get all the coupons from the seg api """
        # self.api = api()
        
        # self.email = "testcacho@test.com"
        # self.password = "asdfgh"
        
        # self.auth_token = self.api.user_login(self.email, self.password)
        
        
        # coupons_results = self.seg_api.get_valid_coupons_by_category(
        #     self.auth_token,
        #     location_id = 4186,
        #     category = "FIXED_AMOUNT_OFF_BASKET",
        # )
        # print(coupons_results)
    
    def rpa_hello_word(self):
        """ This is a simple automation that prints Hello Word """
        log("Hello Word")
        return

    def rpa_set_redeem_points_balance(self):
        """ This automation set the redeem points balance"""
        self.seg_api.set_redeem_points_balance(
            wallet_id = 27557398,
            member_id = "SEG0000005247455",
            credit = 1000
        )

        return
    

    def rpa_create_an_order_by_api(self):
        """ This automation create an order by the api"""

        
    # def rpa_testrail_sync(self):
    #     """This executes the script for TestRail sync"""
    #     print("DUMMY to complete the steps you need here")
    #     print("DUMMY to complete the steps you need here")
    #     print("DUMMY to complete the steps you need here")


if __name__ == '__main__':
    # pass
    rpa = RpaJobs()
    rpa.rpa_get_coupons_from_seg_api()
    
    
    # rpa.rpa_create_an_order_by_api()
    # rpa.rpa_set_provider_in_qaPod4()
    # rpa.rpa_gpt_completion_story_points_in_ticket()
    # rpa.rpa_testrail_sync()

