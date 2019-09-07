import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox",
    )
    parser.addoption(
        "--language", action="store", default="en", help="Choose default locale"
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = ChromeOptions()
        options.add_experimental_option(
            "prefs", {"intl.accept_languages": user_language}
        )
        browser_instance = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("intl.accept_languages", user_language)
        browser_instance = webdriver.Firefox(firefox_profile=firefox_profile)
    else:
        print("Browser {} still is not implemented".format(browser_name))
        browser_instance = None
    browser_instance.implicitly_wait(5)
    yield browser_instance
    time.sleep(5)
    print("\nquit browser..")
    browser_instance.quit()
