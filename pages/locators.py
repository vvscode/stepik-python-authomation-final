from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_EMAIL_FIELD = (By.ID, "id_registration-email")
    REGISTER_PASS1_FIELD = (By.ID, "id_registration-password1")
    REGISTER_PASS2_FIELD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ITEM_ADDED_TO_BASKET = (By.CSS_SELECTOR, ".alert-success strong")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert-info strong")


class BasketPageLocators:
    BASKET_ITEM_LIST = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_TOTAL_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info strong")
