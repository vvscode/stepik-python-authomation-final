from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_exist_login_url()
        self.should_exist_login_form()
        self.should_exist_register_form()

    def should_exist_login_url(self):
        assert "login" in self.browser.current_url, "Login URL is wrong"

    def should_exist_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "Login form is not presented"

    def should_exist_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "Register form is not presented"

    def register_new_user(self, email, password):
        reg_email_field = self.browser.find_element(
            *LoginPageLocators.REGISTER_EMAIL_FIELD
        )
        reg_pass1_field = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASS1_FIELD
        )
        reg_pass2_field = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASS2_FIELD
        )
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)

        reg_email_field.send_keys(email)
        reg_pass1_field.send_keys(password)
        reg_pass2_field.send_keys(password)
        reg_button.click()
