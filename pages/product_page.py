from .base_page import BasePage
from.locators import BasketPageLocators


class ProductPage(BasePage):

    def add_item(self):
        how, what = BasketPageLocators.ADDED_BUTTON_NAME
        if self.is_element_present(how, what):
            self.get_element(how, what).click()

    def should_be_added_item(self):
        self.should_be_item_name()
        self.should_be_item_price()

    def should_be_item_name(self):
        item_name = self.get_element(*BasketPageLocators.ITEM_NAME).text
        added_item_name = self.get_element(*BasketPageLocators.ADDED_ITEM_NAME).text
        assert item_name and added_item_name and item_name == added_item_name, "Имена выбранных товаров не совпадают!"

    def should_be_item_price(self):
        price = self.get_element(*BasketPageLocators.PRICE).text
        added_price = self.get_element(*BasketPageLocators.ADDED_PRICE).text
        assert price and added_price and price == added_price, "Цены выбранных товаров не совпадают!"