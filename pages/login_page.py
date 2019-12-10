from selenium.webdriver.common.by import By
from pages.page import Page


class LoginPage(Page):
    USERNAME_INPUT = (By.ID, "j_username")
    PASSWORD_INPUT = (By.ID, "j_password")
    LOGIN_BUTTON = (By.ID, "loginButton")
    FIRST_LOGIN_BUTTON = (By.PARTIAL_LINK_TEXT, "Pierwsze logowanie")
    PASSWORD_CHANGE_BUTTON = (By.PARTIAL_LINK_TEXT, "Zmiana hasła")

    def enter_username(self, username):
        self.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def click_first_login_button(self):
        self.find_element(*self.FIRST_LOGIN_BUTTON).click()

    def click_password_change_button(self):
        self.find_element(*self.PASSWORD_CHANGE_BUTTON).click()
