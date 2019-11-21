class SessionHelper:

    def __init__(self, app):
        self.app = app

    def open_homepage(self):
        driver = self.app.driver
        driver.maximize_window()
        driver.implicitly_wait(60)
        driver.get("https://shop.by/")
