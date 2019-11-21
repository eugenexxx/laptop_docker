from webium import BasePage, Finds, Find
from selenium.webdriver.common.by import By

class Homepage(BasePage):

    catalog_header = Find(by=By.CLASS_NAME, value="Header__BlockCatalogLink")
    computers_label = Find(by=By.CSS_SELECTOR, value="a[href='/kompyutery/']")
    laptops_accessories_label = Find(by=By.XPATH, value="//a[contains(.,'Ноутбуки и аксессуары')]")
    # laptops_label = Find(by=By.CSS_SELECTOR, value="a[href='/noutbuki/']")
    laptops_label = Find(by=By.LINK_TEXT, value="Ноутбуки")
