import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as Options
from webdriver_manager.chrome import ChromeDriverManager

class TestCases(unittest.TestCase):

    def setUp(cls):
        
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument("--start-maximized")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        service_log_path = "chromedriver.log"
        service_args = ['--verbose']

        # Set up the webdriver and navigate to Google.com
        cls.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            service_args = service_args,
            service_log_path = service_log_path,
            options = options
        )



        cls.driver.get("https://www.google.com/")
        
    
    def tearDown(cls):
        # Close the webdriver after all tests have run
        cls.driver.quit()


    def test_search_box_present(self):
        # Test that the search box is present on the Google homepage
        search_box = self.driver.find_element_by_name("q")
        self.assertIsNotNone(search_box)

    def test_search_for_term(self):
        # Test that a search for "python" returns results
        search_box = self.driver.find_element_by_name("q")
        search_box.send_keys("python")
        search_box.submit()
        result_stats = self.driver.find_element_by_id("result-stats")
        self.assertIsNotNone(result_stats)

    def test_search_suggestions(self):
        # Test that search suggestions are displayed for a partial search term
        search_box = self.driver.find_element_by_name("q")
        search_box.send_keys("pyth")
        suggestion_list = self.driver.find_element_by_class_name("erkvQe")
        suggestions = suggestion_list.find_elements_by_tag_name("li")
        self.assertGreater(len(suggestions), 0)
    
    def test_qaia_first_case(self):
        
        ticket_to_test_description = 
        
        """
        make the necessary changes to be able to search in google for the word 'pedorro' and that the first result is 'English Translation of “pedorro" - Collins Dictionary'
        """
        {
            ticket_definition: '',
            data_page: '',
            commands_history: []
        }


        import os
        from chat_bot import ChatBot

        key = os.environ['OPENAI_API_KEY']

        qaia = ChatBot(message_history=[{"role": "system", "content":
        """
        Act as a Quality Assurance Intelligent Agent
        which:
        
        given a json data with this structure:
        {
            data_page: '',
            history: [],
            note: ''

        }

        ticket_definition: this will have the definition of the ticket
        data_page: this will have the last data object model of a web
        commands_history: is going to contain the history of the selenium commands
        each command has this format driver.<selenium command>
        The Quality Assurance Intelligent Agent should return the next command
        step_note

        """ + ticket_to_test_description}])
        
        
        conversation = first_prompt

        while True:
            conversation = qaia.send_prompt(conversation)
            










        search_box = self.driver.find_element_by_name("q")
        search_box.send_keys("pyth")
        suggestion_list = self.driver.find_element_by_class_name("erkvQe")
        suggestions = suggestion_list.find_elements_by_tag_name("li")
        self.assertGreater(len(suggestions), 0)
    


if __name__ == '__main__':
    unittest.main()
