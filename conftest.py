import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru or other")

@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("language")
    print("\nstart chrome browser for test..")
    options = Options()
    #options.add_argument('--headless')         # если раскоментировать эти две строчки, 
    #options.add_argument('--start-maximized')  # тесты будут запускаться в фоновом режиме
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    browser = webdriver.Chrome(options=options)  
    yield browser
    print("\nquit browser..")
    browser.quit()

    