import os
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# @pytest.fixture(autouse=True)
# def get_driver(request):
#     if os.environ["BROWSER"] == "chrome":
#         options = Options()
#         options.add_argument("--incognito")
#         options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36")
#         options.add_argument("--window-size=1920,1080")
#         options.add_argument("-disable-blink-features=AutomationControlled")
#         driver = webdriver.Chrome(options=options)
#         request.cls.driver = driver
#         yield
#         driver.quit()
#     elif os.environ["BROWSER"] == "safari":
#         driver = webdriver.Safari()
#         request.cls.driver = driver
#         yield
#         driver.quit()
def create_browser(browser_name="chrome"):
    if browser_name == "chrome":
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("-disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options=options)
        return driver
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
        return driver
    elif browser_name == "safari":
        driver = webdriver.Safari()
        return driver


@pytest.fixture()
def browser_factory():
    return create_browser
