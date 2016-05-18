import unittest
from selenium import webdriver
import page

class YouTubeVideoSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://youtube.com")

    def test_search_video(self):
        """
        Tests python.org search feature. Searches for the word "pycon" then verified that some results show up.
        Note that it does not look for any particular text in search results page. This test verifies that
        the results were not empty.
        """

        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Checks if the word "Python" is in title
        assert main_page.is_title_matches(), "youtube.com title doesn't match."
        #Sets the text of search textbox to "pycon"
        main_page.search_text_element = "Introducing GuideSpark's Innovative Platform"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        assert search_results_page.is_results_found(), "No results found."
        assert search_results_page.is_video_available(), "Video not found"
        search_results_page.click_wanted_video()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()