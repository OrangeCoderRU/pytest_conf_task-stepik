import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
    help="Choose language test")

@pytest.fixture(scope="function")
def browser(request):
    language_test = request.config.getoption("language")
    if language_test != None:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language_test})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language ???")
    yield browser
    print("\nquit browser..")
    browser.quit()
