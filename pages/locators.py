from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_OPEN = (By.CSS_SELECTOR, ".btn-group>a")
    EMPTY_BASKET = (By.XPATH, "//p[contains(text(), 'empty')]")

class LoginPageLocators():
    REGISTRATION_LINK = (By.ID, "id_registration-email")
    LOGIN_LINK_A = (By.ID, "id_login-username")
    EMAIL_FIELD = (By.ID, "id_registration-email")
    PASSWORD_FIELD = (By.ID, "id_registration-password1")
    REPEAT_PASSWORD_FIELD = (By.ID, "id_registration-password2")
    SUBMIT_REGISTRATION = (By.NAME, "registration_submit")
    SUCCESS_REGISTRATION = (By.CLASS_NAME, "alertinner")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group>a")
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, "div.alert:nth-child(1) strong")
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    EMPTY_BASKET = (By.XPATH, "//p[contains(text(), 'empty')]")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_PAGE = (By.CSS_SELECTOR, ".btn-group>a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    PRODUCT_IN_BASKET_FORM = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_IS_EMPTY_LOCATOR = (By.CSS_SELECTOR, "#content_inner > p")


