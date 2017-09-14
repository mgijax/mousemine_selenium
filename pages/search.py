from base import BasePage
from base import InvalidPageException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchRegion(BasePage):
    _search_box_locator = 'quickSearchInput'

    def __init__(self, driver):
        super(SearchRegion, self).__init__(driver)

    def searchFor(self, term):
        self.search_field = self.driver.find_element_by_id(self._search_box_locator)
        self.search_field.clear()
        self.search_field.send_keys(term)
        self.search_field.submit()
        return SearchResults(self.driver)


class SearchResults(BasePage):
    _results_locator = 'keywordSearchResults'
    _result_list_locator = 'keywordSearchResult'
    _result_value_locator = 'value'
    _results = []

    def __init__(self, driver):
        super(SearchResults, self).__init__(driver)
        hits = self.driver.find_elements_by_class_name(self._result_list_locator)

        for hit in hits:
            value = str(hit.find_element_by_class_name(self._result_value_locator).text)
            self._results.append(value)



    def _validate_page(self, driver):
        try:
            WebDriverWait(driver, 5).\
            until(EC.presence_of_element_located((By.CLASS_NAME, self._results_locator)))
        except:
            raise InvalidPageException('Search results not loaded')

    @property
    def result_count(self):
        return len(self._results)

    def get_results(self):
        return self._results
