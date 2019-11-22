

    def cheapest_laptop_first(self):
        laptopList1 = self.app.driver.find_elements_by_xpath(ResultsComparison.LIST_LAPTOPS_CHEAPEST)
        global cheapest_laptop_1
        cheapest_laptop_1 = laptopList1[0].text

    def sort_exp_first(self):
        self.app.driver.find_element_by_xpath(ResultsComparison.SORT_OPTIONS_MENU).click()

        wait = WebDriverWait(self.app.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ResultsComparison.SORT_OPTIONS_BLOCK)))
        self.app.driver.find_element_by_xpath(ResultsComparison.SORT_BY_EXPENSIVE).click()

        wait = WebDriverWait(self.app.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, ResultsComparison.BY_EXPENSIVE_LABEL)))

        def open_last_page():
            Pages = self.app.driver.find_elements_by_xpath(ResultsComparison.SEARCH_RESULTS_PAGES)
            Pages[-1].click()
        open_last_page()

    def cheapest_laptop_last(self):
        laptopList2 = self.app.driver.find_elements_by_xpath(ResultsComparison.LIST_LAPTOPS_EXPENSIVE)
        global cheapest_laptop_2
        cheapest_laptop_2 = laptopList2[-1].text

    def compare_results(self):
        if cheapest_laptop_1 == cheapest_laptop_2:
            print('\n     Values are equal: '+ '\n#1 ' + cheapest_laptop_1 + '\n      is equal to' + '\n#2 ' + cheapest_laptop_2)

        else:
            print('\nValues are NOT equal !!!' + '\n' + 'first laptop is - ' + cheapest_laptop_1
                  + '\n' + 'second laptop is - ' + cheapest_laptop_2)