from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_item_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM), \
            "Item is presented, but should not be"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Message about empty basket is not presented"
