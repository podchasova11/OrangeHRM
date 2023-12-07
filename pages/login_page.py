import time
import allure
from data.links import Links
from config.base_page import BasePage

class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    USERNAME_FIELD = "//input[@name='username']"
    PASSWORD_FIELD = "//input[@name='password']"
    LOGIN_BUTTON = "//button[@type='submit']"
    FORGOT_PASSWORD_LINK = "//div[@class='orangehrm-login-forgot']"

    @allure.step("Enter username")
    def enter_username(self, username='Admin'):
        time.sleep(5)
        self.find(self.USERNAME_FIELD).send_keys(username)

    @allure.step("Enter password")
    def enter_password(self, password='admin123'):
        self.find(self.PASSWORD_FIELD).send_keys(password)

    @allure.step("Enter username")
    def click_login_button(self):
        self.find(self.LOGIN_BUTTON).klick()