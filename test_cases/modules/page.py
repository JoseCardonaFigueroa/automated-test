from elements import BasePageElement
from locators import MainPageLocators
from locators import SearchResultsPageLocators
from locators import VideoPageLocators
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'masthead-search-term'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "YouTube" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source

    def is_video_available(self):
        return self.driver.find_element(*SearchResultsPageLocators.WANTED_VIDEO)

    def click_wanted_video(self):
        element = self.driver.find_element(*SearchResultsPageLocators.WANTED_VIDEO)
        element.click()

class VideoPage(BasePage):
    """ Video page action methods """
    def is_play_btn_clickable(self):
        return self.driver.find_element(*VideoPageLocators.PLAY_BTN)

    def click_play_pause_btn(self):
        element = self.driver.find_element(*VideoPageLocators.PLAY_BTN)
        element.click()

    def drag_volume_slider(self):
        volume_element = self.driver.find_element(*VideoPageLocators.VOLUME_SLIDER)
        return volume_element

    def drag_progress_bar(self):
        progress_bar = self.driver.find_element(*VideoPageLocators.PROGRESS_BAR_SLIDER)
        return progress_bar
