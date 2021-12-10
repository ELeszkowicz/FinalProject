from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self):
        WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(MainPageLocators.BASKET_OPEN)).click()
        WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(MainPageLocators.EMPTY_BASKET))
        assert True, "The message about empty basket is not visible"





