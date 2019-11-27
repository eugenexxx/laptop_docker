from pages.results import ResultsPage
from waiting import wait, TimeoutExpired
import logging
import allure

LOGGER = logging.getLogger(__name__)


class ResultsPageActions:
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.results_actions = ResultsPage(driver=self.driver)

    @allure.step('Verify amount of found items')
    def count_items(self):
        LOGGER.info("Verify amount of found items")
        driver = self.app.driver
        driver.implicitly_wait(180)
        items_number = self.results_actions.found_items
        LOGGER.info('Search results: ' + items_number.text + ' items')

    @allure.step('Sort found items by cheapest price')
    def sort_cheap_first(self):
        LOGGER.info("Sort found items by cheapest price")
        driver = self.app.driver
        driver.implicitly_wait(180)
        self.results_actions.sort_options_menu.click()
        wait(lambda: self.results_actions.is_element_present("sort_options_block"), timeout_seconds=20.0)
        self.results_actions.sort_by_cheapest.click()
        wait(lambda: self.results_actions.is_element_present("by_cheapest_label"), timeout_seconds=20.0)

    @allure.step('Verify cheapest laptop name')
    def cheapest_laptop_first(self):
        LOGGER.info("Verify cheapest laptop name")
        driver = self.app.driver
        driver.implicitly_wait(180)
        cheapest_laptop_list = self.results_actions.list_laptops_cheapest
        global cheapest_laptop_first
        cheapest_laptop_first = cheapest_laptop_list[0].text
        LOGGER.info('Cheapest laptop is ' + cheapest_laptop_first)

    @allure.step('Sort found items by highest price')
    def sort_expensive_first(self):
        LOGGER.info("Sort found items by highest price")
        driver = self.app.driver
        driver.implicitly_wait(180)
        self.results_actions.sort_options_menu.click()
        wait(lambda: self.results_actions.is_element_present("sort_options_block"), timeout_seconds=20.0)
        self.results_actions.sort_by_expensive.click()
        wait(lambda: self.results_actions.is_element_present("by_expensive_label"), timeout_seconds=20.0)

    @allure.step('Open last page in search results')
    def open_last_page(self):
        LOGGER.info("Open last page in search results")
        driver = self.app.driver
        driver.implicitly_wait(180)
        Pages = self.results_actions.search_results_pages
        Pages[-1].click()

    @allure.step('Verify cheapest laptop name (last laptop in search results)')
    def cheapest_laptop_last(self):
        LOGGER.info("Verify cheapest laptop name (last laptop in search results)")
        driver = self.app.driver
        driver.implicitly_wait(180)
        cheapest_laptop_list = self.results_actions.list_laptops_expensive
        global cheapest_laptop_last
        cheapest_laptop_last = cheapest_laptop_list[-1].text
        LOGGER.info('Cheapest laptop is ' + cheapest_laptop_last)

    @allure.step('Compare results')
    def compare_results(self):
        LOGGER.info("Compare results")
        driver = self.app.driver
        driver.implicitly_wait(180)
        LOGGER.info("First value is: " + cheapest_laptop_first)
        LOGGER.info("Second value is: " + cheapest_laptop_last)
        assert cheapest_laptop_first == cheapest_laptop_last, \
            LOGGER.info('\nValues are NOT equal !!!' + '\n' + 'first laptop is - '
                        + cheapest_laptop_first + '\n' + 'second laptop is - ' + cheapest_laptop_last)
