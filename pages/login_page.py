from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert LoginPageLocators.PART_URL in self.browser.current_url, "Неверный адрес страницы" # сообщение об ошибке

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Отсутствует форма логина или не верный селектор"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Отсутствует форма регистрации или не верный селектор"
    
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_SUBMIT).click()
                                                                    