from base import BasePage
from base import InvalidPageException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class HomePage(BasePage):

    _home_page_title = 'MouseMine: Home'
    _home_tab_locator = 'home'

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def _validate_page(self, driver):
        home_tab = self.tab_selector.find_element_by_id(self._home_tab_locator)
        home_tab.click()
        try:
            WebDriverWait(driver, 5).until(expected_conditions.title_is(self._home_page_title))
        except:
            raise InvalidPageException("Home Page not loaded")
