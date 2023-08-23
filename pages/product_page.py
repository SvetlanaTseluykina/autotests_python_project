from .base_page import BasePage
from.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_item(self):
        how, what = ProductPageLocators.ADDED_BUTTON_NAME
        if self.is_element_present(how, what):
            self.get_element(how, what).click()

    def should_be_added_item(self):
        self.should_be_item_name()
        self.should_be_item_price()

    def should_be_item_name(self):
        item_name = self.get_element(*ProductPageLocators.ITEM_NAME).text
        added_item_name = self.get_element(*ProductPageLocators.ADDED_ITEM_NAME).text
        assert item_name and added_item_name and item_name == added_item_name, "Имена выбранных товаров не совпадают!"

    def should_be_item_price(self):
        price = self.get_element(*ProductPageLocators.PRICE).text
        added_price = self.get_element(*ProductPageLocators.ADDED_PRICE).text
        assert price and added_price and price == added_price, "Цены выбранных товаров не совпадают!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
