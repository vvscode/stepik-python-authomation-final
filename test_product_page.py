import time
import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.main_page import MainPage


BASE_LINK = "http://selenium1py.pythonanywhere.com/"
ITEM_1_LINK = f"{BASE_LINK}catalogue/the-city-and-the-stars_95/"
ITEM_2_LINK = f"{BASE_LINK}catalogue/coders-at-work_207/"


@pytest.mark.user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = f"{BASE_LINK}accounts/login/"
        page = LoginPage(browser, login_link)
        page.open()
        generated_password = str(time.time())
        generated_email = f"{generated_password}@some-fake.email"
        page.register_new_user(generated_email, generated_password)
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, ITEM_2_LINK)
        product_page.open()
        product_page.should_not_show_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, ITEM_2_LINK)
        product_page.open()
        product_page.add_item_to_basket()
        product_page.should_add_item_to_basket_msg()
        product_page.basket_price_msg_equals_item_price()


@pytest.mark.long
@pytest.mark.need_review
@pytest.mark.parametrize(
    "promo",
    [
        "?promo=newYear2019",
        # "?promo=offer0",
        # "?promo=offer1",
        # "?promo=offer2",
        # "?promo=offer3",
        # "?promo=offer4",
        # "?promo=offer5",
        # "?promo=offer6",
        # pytest.param(
        #     "?promo=offer7", marks=pytest.mark.xfail(reason="We're working on that!")
        # ),
        # "?promo=offer8",
        # "?promo=offer9",
    ],
)
def test_guest_can_add_product_to_basket(browser, promo):
    promo_link = f"{ITEM_2_LINK}{promo}"
    produt_page = ProductPage(browser, promo_link)
    produt_page.open()
    produt_page.add_item_to_basket()
    produt_page.solve_quiz_and_get_code()
    produt_page.should_add_item_to_basket_msg()
    produt_page.basket_price_msg_equals_item_price()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, ITEM_2_LINK)
    product_page.open()
    product_page.should_not_show_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    product_page = ProductPage(browser, ITEM_1_LINK)
    product_page.open()
    product_page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, ITEM_2_LINK)
    product_page.open()
    product_page.should_be_login_link()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, ITEM_2_LINK)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_item_in_basket()
    basket_page.should_be_empty_basket_msg()
