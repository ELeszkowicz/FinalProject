from .product_page import ProductPage
from .base_page import BasePage
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.register_new_user(email_field, password_field)

    def should_be_login_url(self):
        assert "login" in self.open(), "login is absent in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK_A), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_LINK), "Registration form is not presented"

    def register_new_user(self, email_field, password_field):
        WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD)).send_keys(email_field)
        WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(LoginPageLocators.PASSWORD_FIELD)).send_keys(password_field)
        WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(LoginPageLocators.REPEAT_PASSWORD_FIELD)).send_keys(password_field)
        WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(LoginPageLocators.SUBMIT_REGISTRATION)).click()
        assert self.is_element_present(*LoginPageLocators.SUCCESS_REGISTRATION), "Registration is not successed"
