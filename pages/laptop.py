from webium import BasePage, Finds, Find
from selenium.webdriver.common.by import By


class LaptopSearchPage(BasePage):
    model_list_checkboxes = Finds(by=By.XPATH, value='//*[@id="Attr_prof_1000"]//label')
    diagonal_list_checkboxes = Finds(by=By.XPATH, value='//*[@id="Attr_prof_5828"]//label')
    diagonal_block = Find(by=By.CSS_SELECTOR, value='div.ModelFilter__TipAttrWapper:nth-child(7)')
    show_results_button = Find(by=By.XPATH, value="//div[@data-param='filter_buttons']"
                                                  "//span[@class='ModelFilter__CountItems']")
    price_from_button = Find(by=By.XPATH, value="//input[@id='minnum_45']")
    price_to_button = Find(by=By.XPATH, value="//input[@id='maxnum_45']")
    diagonal_block_extended = Find(by=By.CSS_SELECTOR, value='#Attr_prof_5828')
    laptops_block_extended = Find(by=By.CSS_SELECTOR, value='#Attr_prof_1000')
    model_list_expand = Find(by=By.CSS_SELECTOR, value="span[data-idgroup='prof_1000']")
    close_button = Find(by=By.XPATH, value="//a[@data-ga='sbros']")
