def test_laptops(app):
    # Open homepage shop.by in browser, maximize window
    app.session.open_homepage()
    assert "Торговый портал Shop.by – Все интернет-магазины Минска и Беларуси" in app.driver.title

    # Click Laptop catalog on Homepage
    app.steps.homepage_clicks()

    # Input search options in Laptop catalog
    app.steps.set_price(price_from='700', price_to='2500')
    app.steps.select_model(value=['Dell', 'Lenovo', 'HP'])
    app.steps.select_diagonal(lowest_value='12.0', highest_value='13.4')
    app.steps.show_results()
    assert "Ноутбук купить в Минске, цены на ноутбуки и нетбуки в интернет-магазинах – Shop.by" in app.driver.title

    # Validate amount of items on the page
    app.steps.count_items()

    # Sort results by price (lowest price first) and validate cheapest laptop
    app.steps.sort_cheap_first()
    app.steps.cheapest_laptop_first()

    # Sort results by price (highest price first) and validate last
    # laptop on the last page of search results
    app.steps.sort_exp_first()
    app.steps.cheapest_laptop_last()

    # Compare results
    app.steps.compare_results()
