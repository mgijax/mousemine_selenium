import unittest
from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        # navigate to MouseMine home page
        self.driver.get('http://www.mousemine.org/')

    def tearDown(self):
        # close the browser window
        self.driver.quit()
