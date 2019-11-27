from fixture.session import SessionHelper
from steps.homepage_steps import HomepageActions
from steps.catalog_steps import CatalogActions
from steps.results_steps import ResultsPageActions
import webium.settings
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import webium.settings
import logging

LOGGER = logging.getLogger(__name__)


class Application:
    def __init__(self, browser, base_url, config):
        # Set browser
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--disable-application-cache")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--window-size=1420,1080')
            self.driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=chrome_options)
        elif browser == "ie":
            self.driver = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        # Sets a sticky timeout to implicitly wait for an element to be found
        self.driver.implicitly_wait(60)
        webium.settings.wait_timeout = 30
        # Invokes the window manager-specific 'full screen' operation
        LOGGER.info("Expand browser to full screen")
        self.driver.maximize_window()
        # Delete all cookies in the scope of the session
        self.driver.delete_all_cookies()
        # Initialize pages
        LOGGER.info("Started execution test")
        self.session = SessionHelper(self)
        self.homepage = HomepageActions(self)
        self.searching = CatalogActions(self)
        self.results = ResultsPageActions(self)
        self.base_url = "https://www.shop.by/"

    def open_home_page(self):
        LOGGER.info("Open url '%s'", self.base_url)
        driver = self.driver
        driver.get(self.base_url)

    # Stop the browser
    def destroy(self):
        LOGGER.info("Quits the driver and closes every associated window.")
        self.driver.quit()

    def is_valid(self):
        try:
            self.current_url()
            LOGGER.info("Browser is valid")
            return True
        except WebDriverException:
            return False

    def current_url(self):
        return self.driver.current_url
