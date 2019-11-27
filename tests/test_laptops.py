from conftest import capture_screenshot
import pytest
import time

@capture_screenshot
def test_laptop_search(app):

    current_time = time.strftime("%d/%m/%Y %H:%M:%S")
    app.session.open_homepage()
    assert "Торговый портал Shop.by – Все интернет-магазины Минска и Беларуси" in app.driver.title
    app.homepage.expand_main_menu()
    app.homepage.expand_computers_menu()
    app.homepage.expand_laptops_menu()
    app.homepage.click_laptops()
    assert "Ноутбук купить в Минске, цены на ноутбуки и нетбуки в интернет-магазинах – Shop.by" in app.driver.title

    app.searching.disable_search_button()
    app.searching.set_price(price_from='700', price_to='2500')
    app.searching.select_model(value=['Dell', 'Lenovo', 'HP'])
    app.searching.select_diagonal(lowest_value='12.0', highest_value='13.4')
    time.sleep(10)
    app.searching.show_results()
    assert "Ноутбук купить в Минске, цены на ноутбуки и нетбуки в интернет-магазинах – Shop.by" in app.driver.title

    app.results.count_items()
    app.results.sort_cheap_first()
    app.results.cheapest_laptop_first()
    app.results.sort_expensive_first()
    app.results.open_last_page()
    app.results.cheapest_laptop_last()
    app.results.compare_results()
