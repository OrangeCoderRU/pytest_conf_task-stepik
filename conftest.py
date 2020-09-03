import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
    help="Choose language test")

@pytest.fixture(scope="function")
def browser(request):
    language_test = request.config.getoption("language")
    if language_test != None:
        browser = webdriver.Chrome()
    else:
        raise pytest.UsageError("--language ???")
    yield browser
    print("\nquit browser..")
    browser.quit()
