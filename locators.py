from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'masthead-search-term')



class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    WANTED_VIDEO = (By.XPATH, '//*[@title="Introducing GuideSpark\'s Innovative Platform"]')
