from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REGISTATION_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REGISTRATION_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_REGISTRATION_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    ADDED_ITEM_NAME = (By.CSS_SELECTOR, ".alert:nth-child(1) > div:nth-child(2) > strong")
    ITEM_NAME = (By.CSS_SELECTOR, '[class="col-sm-6 product_main"] > h1')
    ADDED_BUTTON_NAME = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
    PRICE = (By.CSS_SELECTOR, "p.price_color:nth-child(2)")
    ADDED_PRICE = (By.CSS_SELECTOR, "div.alert:nth-child(3) > div:nth-child(2) > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1) > div")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "[class^='basket-mini'] > span")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    ITEM = (By.CSS_SELECTOR, "[class='basket-items']")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "[class='content'] > div > p")
