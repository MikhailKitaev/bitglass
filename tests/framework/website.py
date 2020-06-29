import os
from selenium import webdriver
from data.config import settings
from urllib.parse import urljoin
from selenium.webdriver.chrome.options import Options


class Website:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Website()
        return cls.instance

    def __init__(self):
        if str(settings['browser']).lower() == "firefox":
            self.driver = webdriver.Firefox()
            firefox_driver = "./chromedriver";
            self.driver = webdriver.Chrome(firefox_options=options, executable_path=firefox_driver)
        elif str(settings['browser']).lower() == "chrome":
            chrome_options = Options()
            # chrome_options.add_argument('--no-sandbox')
            # chrome_options.add_argument("--headless")
            chrome_options.add_argument(settings['resolution'])
            chrome_driver = "/Users/mikhail/PycharmProjects/bitglass/chromedriver";
            self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
            # self.driver.implicitly_wait(10)
        else:
            self.driver = webdriver.Firefox()


    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get(settings['url'])

    def goto_page(self, page):
        self.driver.get(urljoin(settings['url'], page.lower()))

    def verify_component_exists(self, component):
        # Simple implementation
        assert component in self.driver.find_element_by_tag_name('body').text, \
            "Component {} not found on page".format(component)

    def __del__(self):
        self.driver.quit()


website = Website.get_instance()
