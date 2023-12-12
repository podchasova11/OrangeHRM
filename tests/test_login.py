# import time
#
# import allure
# import pytest
# from config.base_test import BaseTest
# from data.links import Links
# from pages.login_page import LoginPage
#
#
# class TestLogin(BaseTest):
#
#     @allure.title("Login in CRM")
#     def test_login(self):
#         self.login_page().open()
#         self.login_page().is_opened()
#         self.login_page().enter_username("Admin")
#         self.login_page().enter_password("admin123")
#         self.login_page().click_login_button()


import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from config.base_test import BaseTest
from data.links import Links
from pages.login_page import LoginPage


# @pytest.mark.usefixtures("get_driver")
@allure.feature("Login_and_go_to_site")
class TestLogin(BaseTest):

    def setup(self):
        self.login_page = LoginPage(BaseTest)

    def test_successful_login(self):
        self.login_page.open()
        self.login_page.enter_username('Admin')
        self.login_page.enter_password('admin123')
        self.login_page.click_login_button()