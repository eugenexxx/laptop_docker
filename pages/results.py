from webium import BasePage, Finds, Find
from selenium.webdriver.common.by import By


class ResultsPage(BasePage):
    found_items = Find(by=By.XPATH, value="//span[@class='ModelFilter__CountItems']")
    sort_options_menu = Find(by=By.XPATH, value="//b[@class='chzn-btn glyphicon']")
    sort_options_block = Find(by=By.CSS_SELECTOR, value=".chzn-results")
    sort_by_cheapest = Find(by=By.XPATH, value="//li[contains(.,'С дешевых')]")
    sort_by_expensive = Find(by=By.XPATH, value="//li[contains(.,'С дорогих')]")
    by_cheapest_label = Find(by=By.XPATH, value="//span[contains(.,'С дешевых')]")
    by_expensive_label = Find(by=By.XPATH, value="//span[contains(.,'С дорогих')]")
    list_laptops_cheapest = Finds(by=By.XPATH, value="//*[@class='PageTip__DataList Page__DataList']"
                                                     "//span[@itemprop='name']")
    list_laptops_expensive = Finds(by=By.XPATH, value="//*[@class='PageTip__DataList Page__DataList']"
                                                      "//span[@itemprop='name']")
    search_results_pages = Finds(by=By.XPATH, value="//*[@class='Paging__InnerPages']"
                                                    "//a[@class='Paging__PageLink hidden-xs']")
