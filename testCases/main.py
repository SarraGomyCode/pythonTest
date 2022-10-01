import unittest
from selenium import webdriver
import page


class PythonOrgSearch (unittest.TestCase):

    def setUp(self):
        PATH = r"/chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        self.driver.get("https://www.python.org/")


    def test_matched_text(self):
        main_page = page.MainPage()
        assert main_page.is_it_matched()

    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()
