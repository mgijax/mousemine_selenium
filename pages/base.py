from abc import abstractmethod


class BasePage(object):
    """ All page objects inherit from this """

    _tab_container_locator = 'menucontainer'

    def __init__(self, driver):
        self.tab_selector = driver.find_element_by_id(self._tab_container_locator)
        self._validate_page(driver)
        self.driver = driver

    @abstractmethod
    def _validate_page(self, driver):
        return

    """ Regions define functionality available through all page objects """
    @property
    def search(self):
        from search import SearchRegion
        return SearchRegion(self.driver)

    @property
    def templates(self):
        from templatespage import TemplatesPage
        return TemplatesPage(self.driver)

    @property
    def lists(self):
        from listspage import ListsPage
        return ListsPage(self.driver)

class InvalidPageException(Exception):
    """ Throw this exception when you don't find the correct page """
    pass
