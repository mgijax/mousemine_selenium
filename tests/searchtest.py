from ddt import ddt, data, unpack
import sys
sys.path.append("..")
from pages.homepage import HomePage
from base.basetestcase import BaseTestCase
from helpers.filedatahelper import get_data


@ddt
class QuickSearchTest(BaseTestCase):
    testingdata = get_data('testdata/QuickSearchTestData.xlsx')
    @data(*testingdata)
    @unpack
    def test_QuickSearch(self, search_value, expected_result, notes):
        homepage = HomePage(self.driver)
        search_results = homepage.search.searchFor(search_value)
        self.assertTrue(expected_result in search_results.get_results())

if __name__ == '__main__':
    unittest.main(verbosity=2)
