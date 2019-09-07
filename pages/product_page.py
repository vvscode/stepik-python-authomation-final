import math
from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x_value = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x_value))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print(f"Your code: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_item_name(self):
        assert self.is_element_present(
            *ProductPageLocators.ITEM_NAME
        ), "Item name is not presented"
        return self.browser.find_element(*ProductPageLocators.ITEM_NAME).text

    def get_item_price(self):
        assert self.is_element_present(
            *ProductPageLocators.ITEM_PRICE
        ), "Item price is not presented"
        return self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text

    def add_item_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_add_item_to_basket_msg(self):
        book_name = self.get_item_name()
        added_book = self.browser.find_element(
            *ProductPageLocators.ITEM_ADDED_TO_BASKET
        ).text
        assert (
            added_book == book_name
        ), "Book added to basket differs from current book name"

    def basket_price_msg_equals_item_price(self):
        item_price = self.get_item_price()
        basket_total = self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL_PRICE
        ).text
        assert item_price == basket_total, "Basket total is differs from Item price"

    def should_not_show_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.ITEM_ADDED_TO_BASKET
        ), "Successfully added to basket message appears without any action"

    def disappeared_success_message(self):
        assert self.is_element_disappeared(
            *ProductPageLocators.ITEM_ADDED_TO_BASKET
        ), "Success message is not disappeared"
