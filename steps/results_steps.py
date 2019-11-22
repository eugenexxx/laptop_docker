from pages.results import ResultsPage
from selenium.webdriver.common.action_chains import ActionChains
from waiting import wait, TimeoutExpired
import logging

LOGGER = logging.getLogger(__name__)


class ResultsPageActions:
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.results_actions = ResultsPage(driver=self.driver)

    def count_items(self):
        LOGGER.info("Verify amount of found items")
        driver = self.app.driver
        driver.implicitly_wait(180)
        items_number = self.results_actions.found_items
        print('\n' + 'Search results: ' + items_number.text + ' items')
        LOGGER.info('Search results: ' + items_number.text + ' items')

    def sort_cheap_first(self):
        LOGGER.info("Sort found items by cheapest price")
        driver = self.app.driver
        driver.implicitly_wait(180)
        self.results_actions.sort_options_menu.click()
        wait(lambda: self.results_actions.is_element_present("sort_options_block"), timeout_seconds=20.0)
        self.results_actions.sort_by_cheapest.click()
        wait(lambda: self.results_actions.is_element_present("by_cheapest_label"), timeout_seconds=20.0)

    def cheapest_laptop_first(self):
        LOGGER.info("Verify cheapest laptop name")
        driver = self.app.driver
        driver.implicitly_wait(180)
        cheapest_laptop_list = self.results_actions.list_laptops_cheapest
        global cheapest_laptop_first
        cheapest_laptop_first = cheapest_laptop_list[0].text
        LOGGER.info('Cheapest laptop is ' + cheapest_laptop_first)
