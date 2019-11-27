import allure
from pages.laptop import LaptopSearchPage
from waiting import wait, TimeoutExpired
import logging

LOGGER = logging.getLogger(__name__)


class CatalogActions:
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.catalog_actions = LaptopSearchPage(driver=self.driver)

    @allure.step('Disable search button')
    def disable_search_button(self):
        LOGGER.info("Disable search button")
        found_products = self.catalog_actions.show_results_button
        self.driver.execute_script("return arguments[0].style.display = 'table-footer-group';", found_products)

    @allure.step('Set price')
    def set_price(self, price_from, price_to):
        LOGGER.info("Set price")
        self.catalog_actions.price_from_button.send_keys(price_from)
        self.catalog_actions.price_to_button.send_keys(price_to)

    @allure.step('Select models')
    def select_model(self, value):
        LOGGER.info("Expand model list")
        self.catalog_actions.model_list_expand.click()
        wait(lambda: self.catalog_actions.is_element_present("laptops_block_extended"), timeout_seconds=20.0)
        LOGGER.info("Check corresponding model checkboxes")
        model_list = self.catalog_actions.model_list_checkboxes
        for item in model_list:
            if item.text in value:
                item.click()

    @allure.step('Select diagonal')
    def select_diagonal(self, lowest_value, highest_value):
        LOGGER.info("Expand diagonal list")
        self.driver.execute_script("document.querySelector('span[data-idgroup="'prof_5828'"]').click();")
        wait(lambda: self.catalog_actions.is_element_present("diagonal_block_extended"), timeout_seconds=20.0)
        LOGGER.info("Select diagonal values")
        diagonal_list = self.catalog_actions.diagonal_list_checkboxes
        view_element = self.catalog_actions.diagonal_block
        self.driver.execute_script("return arguments[0].scrollIntoView(0, 200);", view_element)
        for item in diagonal_list:
            if lowest_value <= item.text <= highest_value:
                item.click()

    @allure.step('Show results')
    def show_results(self):
        LOGGER.info("Click button to see results")
        wait(lambda: self.catalog_actions.is_element_present("close_button"), timeout_seconds=20.0)
        self.catalog_actions.show_results_button.click()
