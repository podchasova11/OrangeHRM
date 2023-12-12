from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from libs.helper import Helper
from data.credentials import Credentials
from pages.login_page import LoginPage
# from pages.dashboard_page import DashboardPage

class BaseTest:

    def setup(self):
    self.login_page = LoginPage(self.driver)


    # def setup(self):
    #     self.login_page = LoginPage(self.driver)
    #
    #     # Libs
    #     self.helper = Helper





