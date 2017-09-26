import sys
sys.path.append("..")
from pages.homepage import HomePage
from base.basetestcase import BaseTestCase

class TemplatesPageTest(BaseTestCase):
    def test_VerifyAllTemplatesProduceResults(self):
        homepage = HomePage(self.driver)
        templatespage = homepage.templates

        for template_name in templatespage.get_templates().iterkeys():
            templatequerypage = templatespage.open_template_query(template_name)
            queryresultspage = templatequerypage.show_results

            self.assertTrue(queryresultspage.has_results, "There are no results for templete: " + template_name)




if __name__ == '__main__':
    unittest.main(verbosity=2)
