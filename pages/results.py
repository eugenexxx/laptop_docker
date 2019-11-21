class ResultsComparison:

    SORT_OPTIONS_MENU = '//b[@class="chzn-btn glyphicon"]'
    SORT_OPTIONS_BLOCK = ".chzn-results"
    SORT_BY_CHEAPEST = "//li[contains(.,'С дешевых')]"
    SORT_BY_EXPENSIVE = "//li[contains(.,'С дорогих')]"
    BY_CHEAPEST_LABEL = "//span[contains(.,'С дешевых')]"
    BY_EXPENSIVE_LABEL = "//span[contains(.,'С дорогих')]"
    LIST_LAPTOPS_CHEAPEST = '//*[@class="PageTip__DataList Page__DataList"]//span[@itemprop="name"]'
    LIST_LAPTOPS_EXPENSIVE = '//*[@class="PageTip__DataList Page__DataList"]//span[@itemprop="name"]'
    SEARCH_RESULTS_PAGES = '//*[@class="Paging__InnerPages"]//a[@class="Paging__PageLink hidden-xs"]'
    FOUND_ITEMS = '//span[@class="ModelFilter__CountItems"]'
