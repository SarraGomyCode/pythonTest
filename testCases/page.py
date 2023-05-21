from locator import *

class BasePage(object):

    def __init__ (self,driver):
        self.driver = driver

class MainPage(BasePage):

    def is_it_matched (self):
        return "Python" in self.driver.title

    def click_go_button (self):
        element = self.driver.find_element(MainPageLocators.GO_BUTTON)
        element.click()

class SearchPageResults :

    def is_results_find (self) :

        return "no result" not in self.driver.page_source
