from base import BasePage
from base import InvalidPageException
from templatequerypage import TemplateQueryPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TemplatesPage(BasePage):

    _templates_page_title = 'MouseMine: Template queries page'
    _menu_locator = 'menucontainer'
    _templates_tab_locator = 'templates'

    _template_title_locator = 'templateTitle'
    _templates = {}


    def __init__(self, driver):
        super(TemplatesPage, self).__init__(driver)

        template_elements = driver.find_elements_by_class_name(self._template_title_locator)
        for template in template_elements:
            template_name = template.text.replace(' ','')
            self._templates[template_name] = template.get_attribute('href')

    def _validate_page(self, driver):
        templates_tab = driver.find_element_by_id(self._menu_locator).find_element_by_id(self._templates_tab_locator)
        templates_tab.click()
        try:
            WebDriverWait(driver, 5).until(expected_conditions.title_is(self._templates_page_title))
        except:
            raise InvalidPageException("Templates Page not loaded")

    def get_templates(self):
        return self._templates

    def open_template_query(self, template_name):
        self.driver.get(self._templates[template_name])
        return TemplateQueryPage(self.driver)

