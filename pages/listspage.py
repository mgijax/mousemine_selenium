from base import BasePage
from base import InvalidPageException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def getDropdownList(driver, id_locator):
    dd_selector = driver.find_element_by_id(id_locator)
    dd_select = Select(dd_selector)
    dd_list = [o.text for o in dd_select.options]
    return (dd_selector, dd_select, dd_list)


class ListsPage(BasePage):

    _lists_page_title = 'MouseMine: Lists'
    _list_tab_locator = 'bags'
    _type_selector_locator = 'typeSelector'
    _organism_selector_locator = 'extraConstraintSelect'

    _type_selector = None
    _type_select = None
    _type_list = []
    _organism_selector = None
    _organism_select = None
    _organism_list = []


    def __init__(self, driver):
        super(ListsPage, self).__init__(driver)

        (self._type_selector, self._type_select, self._type_list) = getDropdownList(driver, self._type_selector_locator)
        (self._organism_selector, self._organism_select, self._organism_list) = getDropdownList(driver, self._organism_selector_locator)


    def _validate_page(self, driver):
        list_tab = self.tab_selector.find_element_by_id(self._list_tab_locator)
        list_tab.click()
        try:
            WebDriverWait(driver, 5).until(expected_conditions.title_is(self._lists_page_title))
        except:
            raise InvalidPageException("Lists Page not loaded")

    @property
    def type_count(self):
        return len(self._type_list)

    @property
    def type_getSelected(self):
        return self._type_select.first_selected_option.text

    @property
    def organism_count(self):
        return len(self._organism_list)

    @property
    def organism_getSelected(self):
        return Select(self._organism_selector).first_selected_option.text


