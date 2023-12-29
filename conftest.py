import os
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True, scope="function")
def driver(request):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(autouse=True)
def get_driver(request):
    if os.environ["BROWSER"] == "chrome":
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("-disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options=options)
        request.cls.driver = driver
        yield
        driver.quit()
    elif os.environ["BROWSER"] == "safari":
        driver = webdriver.Safari()
        request.cls.driver = driver
        yield
        driver.quit()


def create_browser(driver="chrome"):
    if driver == "chrome":
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options=options)
        return driver
    elif driver == "firefox":
        driver = webdriver.Firefox()
        return driver
    elif driver == "safari":
        driver = webdriver.Safari()
        return driver


@pytest.fixture()
def browser_factory():
    return create_browser


# @pytest.fixture(autouse=True, scope="class")
# def get_driver(request):
#     # service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome()
#     request.cls.driver = driver
#     yield
#     driver.quit()


# import time

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

options = Options
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36")
driver = webdriver.Chrome(options=options)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
