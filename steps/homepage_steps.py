from pages.homepage import Homepage
from selenium.webdriver.common.action_chains import ActionChains
from waiting import wait, TimeoutExpired
import logging

LOGGER = logging.getLogger(__name__)


class HomepageActions:
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.hp_actions = Homepage(driver=self.driver)

    def expand_main_menu(self):
        LOGGER.info("Expand main menu")
        driver = self.app.driver
        driver.implicitly_wait(180)
        menu_hover = self.hp_actions.catalog_header
        actions = ActionChains(driver)
        actions.move_to_element(menu_hover).perform()
        wait(lambda: self.hp_actions.is_element_present("computers_label"), timeout_seconds=20.0)

    def expand_computers_menu(self):
        LOGGER.info("Expand computers menu")
        driver = self.app.driver
        driver.implicitly_wait(180)
        menu_hover = self.hp_actions.computers_label
        actions = ActionChains(driver)
        actions.move_to_element(menu_hover).perform()
        wait(lambda: self.hp_actions.is_element_present("laptops_accessories_label"), timeout_seconds=20.0)

    def expand_laptops_menu(self):
        LOGGER.info("Expand computers menu")
        driver = self.app.driver
        driver.implicitly_wait(180)
        menu_hover = self.hp_actions.laptops_accessories_label
        actions = ActionChains(driver)
        actions.move_to_element(menu_hover).perform()
        wait(lambda: self.hp_actions.is_element_present("laptops_label"), timeout_seconds=20.0)

    def click_laptops(self):
        LOGGER.info("Click 'Ноутбуки' menu item")
        driver = self.app.driver
        driver.implicitly_wait(10)
        actions = ActionChains(driver)
        laptops_label = self.hp_actions.laptops_label
        actions.move_to_element(laptops_label).perform()
        laptops_label.click()
