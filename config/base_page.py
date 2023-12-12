import allure
from libs.helper import Helper
from selenium.webdriver.support import expected_conditions as EC
from config.base_test import BaseTest


class BasePage(Helper):

    # def open(self):
    #     with allure.step(f"Open {self.PAGE_URL} page"):
    #         self.driver.get(self.PAGE_URL)
    #
    # def is_opened(self, url=None):
    #     url = self.PAGE_URL if url is None else url
    #     with allure.step(f"Page {url} is opened"):
    #         self.wait.until(EC.url_to_be(url))




    # Тут описываются локаторы

    # Тут описываются локаторы
    # LOGOUT_BUTTON = ("xpath", "//button[@id='logout']")
    # LOGO_LINK = ("xpath", "//a[@id='logo']")

    STAGE = "https://opensource-demo.orangehrmlive.com/web/index.php"

    LOGIN_PAGE = f"{STAGE}/auth/login"
    DASHBOARD_PAGE = f"{STAGE}/dashboard/index"

    # # Тут создаются необходимые обьекты, которые будут доступны в pages
    # def __init__(self, driver):
    #     self.driver: WebDriver = driver
    #     self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)
    #     self.helper = Helper

    # Данный метод будет вызываться для любой страницы, принимая ее PAGE_URL
    def open(self):      # "этот метод явл тестовым шагом, поэтому маркируем его аллюром:
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)

    # Ниже описываются общие для всех страниц методы
    def find(self, locator):
        return self.driver.find_element("xpath", locator)
    # "эти методы не явл тестовым шагом, поэтому не маркируем их аллюром:


    # метод, который ждет, пока элемент найдется,
    # return -
    #делает так, что этот метод возвзащает найденный элемент и тогда
    #уже в login_page можно кликать на этот вызванный элемент или
    # делать что-то еще с ним
    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located("xpath", locator))
