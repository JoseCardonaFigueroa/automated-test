from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    #SEARCH_BAR = (By.ID, 'masthead-search-term')
    GO_BUTTON = (By.ID, 'search-btn')


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    WANTED_VIDEO = (By.XPATH, '//*[@title="Introducing GuideSpark\'s Innovative Platform"]')

class VideoPageLocators(object):
    """ A class for video locators. All video locators should come here """
    PLAY_BTN = (By.CLASS_NAME, 'ytp-play-button')
    VOLUME_SLIDER = (By.CLASS_NAME, 'ytp-volume-slider-handle')
    PROGRESS_BAR_SLIDER = (By.CLASS_NAME, 'ytp-scrubber-pull-indicator')
