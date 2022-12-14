from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
#login_form
class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REG_FORM = (By.ID, "register_form")
    PART_URL = "login"
    LOGIN_USERNAME = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    LOGIN_SUBMIT = (By.NAME, "login_submit")
    REG_EMAIL = (By.ID, "id_registration_email")
    REG_PASSWORD1 = (By.ID, "id_registration_pasword1")
    REG_PASSWORD2 = (By.ID, "id_registration_pasword2")
    REG_SUBMIT = (By.NAME, "registration_submit")

