import sys
sys.path.append("..")
from pages.homepage import HomePage
from base.basetestcase import BaseTestCase


class ListsPageTest(BaseTestCase):
    def test_VerifyListsDropdownMenus(self):
        homepage = HomePage(self.driver)
        listspage = homepage.lists

        self.assertGreater(listspage.type_count, 0, "There are no options in Type Dropdown Menu")
        self.assertEquals(listspage.type_getSelected, "Gene", "Gene is not selected in Type Dropdown Menu")

        self.assertGreater(listspage.organism_count, 0, "There are no options in Organism Dropdown Menu")
        self.assertEquals(listspage.organism_getSelected, "M. musculus", "M. musculus is not selected in Organism Dropdown Menu")


if __name__ == '__main__':
    unittest.main(verbosity=2)
