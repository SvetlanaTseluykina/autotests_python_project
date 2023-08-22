from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class BasketPageLocators():
    ADDED_ITEM_NAME = (By.CSS_SELECTOR, ".alert:nth-child(1) > div:nth-child(2) > strong")
    ITEM_NAME = (By.CSS_SELECTOR, '[class="col-sm-6 product_main"] > h1')
    ADDED_BUTTON_NAME = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
    PRICE = (By.CSS_SELECTOR, "p.price_color:nth-child(2)")
    ADDED_PRICE = (By.CSS_SELECTOR, "div.alert:nth-child(3) > div:nth-child(2) > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1) > div")