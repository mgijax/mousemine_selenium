from base import BasePage
from base import InvalidPageException
from queryresultspage import QueryResultsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TemplateQueryPage(BasePage):

    _template_query_page_title = 'MouseMine: Template query:'
    _show_results_button_locator = 'showResultsButton'

    _show_results_button_selector = None


    def __init__(self, driver):
        super(TemplateQueryPage, self).__init__(driver)
        self._show_results_button_selector = driver.find_element_by_id(self._show_results_button_locator)


    def _validate_page(self, driver):
        try:
            WebDriverWait(driver, 5).until(expected_conditions.title_contains(self._template_query_page_title))
        except:
            raise InvalidPageException("Template Query Page not loaded")


    @property
    def show_results(self):
        self._show_results_button_selector.click()
        return QueryResultsPage(self.driver)

