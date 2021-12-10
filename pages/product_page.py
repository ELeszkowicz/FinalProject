from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.test_guest_can_add_product_to_basket()
        self.test_guest_cant_see_success_message_after_adding_product_to_basket()
        self.test_guest_cant_see_success_message()
        self.test_message_disappeared_after_adding_product_to_basket()
        self.test_guest_should_see_login_link_on_product_page()
        self.test_guest_should_see_login_link_from_product_page()
        self.test_guest_cant_see_product_in_basket_opened_from_product_page()

    def test_guest_can_add_product_to_basket(self):
        book_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

        WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET)).click()
        self.solve_quiz_and_get_code()
        print(f"Product {book_name} add to basket, price {book_price}")
        time.sleep(3)
        book_price_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_BASKET).text
        book_name_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_BASKET).text
        print(f"Product {book_name_basket} in basket, price in basket is {book_price_basket}")
        assert book_name == book_name_basket, "Product name in product page and product name in basket didn`t match"
        assert book_price == book_price_basket, "Product price in product page and product price in basket didn`t match"

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET)).click()
        self.solve_quiz_and_get_code()
        time.sleep(3)
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_BASKET), \
            "Success message is presented, but should not be"

    def test_guest_cant_see_success_message(self):
        WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET))
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_BASKET), \
            "Success message is presented, but should not be"

    def test_message_disappeared_after_adding_product_to_basket(self):
        WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET)).click()
        self.solve_quiz_and_get_code()
        time.sleep(3)
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_BASKET), \
            "Success message is presented, but should not be"

    def test_guest_should_see_login_link_on_product_page(self):
        WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET))
        assert True, "Cant see login link on product page"

    def test_guest_should_see_login_link_from_product_page(self):
        WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(BasePageLocators.LOGIN_LINK))
        assert True, "There is no way to registration from product page"

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self):
        WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(ProductPageLocators.BASKET_LINK)).click()
        WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(ProductPageLocators.EMPTY_BASKET))
        assert True, "The message about empty basket is not visible"








