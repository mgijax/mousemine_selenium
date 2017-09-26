from base import BasePage
from base import InvalidPageException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class QueryResultsPage(BasePage):

    _query_results_page_title = 'MouseMine: Query Results'
    _no_results_table_empty_locator = 'im-empty-apology'

    _no_results_table_empty_selector = None


    def __init__(self, driver):
        super(QueryResultsPage, self).__init__(driver)
        self._no_results_table_empty_selector = driver.find_elements_by_id(self._no_results_table_empty_locator)


    def _validate_page(self, driver):
        try:
            WebDriverWait(driver, 5).until(expected_conditions.title_is(self._query_results_page_title))
        except:
            raise InvalidPageException("Query Results Page not loaded")


    @property
    def has_results(self):
        return (len(self._no_results_table_empty_selector) == 0)

