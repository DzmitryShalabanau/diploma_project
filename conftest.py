import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOption
from selenium.webdriver.firefox.options import Options as FirefoxOption
from selenium.webdriver.edge.options import Options as EdgeOption
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from data import TEST_USER
from pages import LoginPage, PersonalCabinetPage


def pytest_addoption(parser):
    parser.addoption('--headless',
                     default='False',
                     help='headless options: "yes" or "no"')
    parser.addoption('--b',
                     default='chrome',
                     help='option to define type of browser')


def create_chrome(headless=True):
    chrome_option = ChromeOption()
    if headless == 'True':
        chrome_option.add_argument('--headless')
        chrome_option.add_argument('window-size=1900x1600')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_option)
    return driver


def create_firefox(headless=True):
    ff_option = FirefoxOption()
    if headless == 'True':
        ff_option.add_argument('--headless')
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=ff_option)
    return driver


def create_edge(headless=True):
    edge_option = EdgeOption()
    if headless == 'True':
        edge_option.add_argument('--headless')
        edge_option.add_argument('window-size=1900x1600')
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_option)
    return driver


@pytest.fixture(autouse=True)
def driver(request):
    driver = None
    browser = request.config.getoption('--b')
    headless = request.config.getoption('--headless')

    print(headless)
    if browser == 'chrome':
        driver = create_chrome(headless)
    if browser == 'ff':
        driver = create_firefox(headless)
    if browser == 'edge':
        driver = create_edge(headless)

    driver.implicitly_wait(5)
    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def open_main_page(request):
    login = LoginPage(request.node.funcargs['driver'])
    login.open()


@pytest.fixture(autouse=False)
def login(request):
    login = LoginPage(request.node.funcargs['driver'])
    login.login(TEST_USER)


@pytest.fixture(scope='function')
def delete_shop(driver):
    print('Adding favorite shop')
    yield
    cabinet = PersonalCabinetPage(driver)
    cabinet.delete_favorite_shop()


@pytest.fixture(scope='function')
def delete_address(driver):
    print('Adding new address')
    yield
    cabinet = PersonalCabinetPage(driver)
    cabinet.click_on_delivery_address()
    cabinet.delete_address()
    cabinet.confirm_delete_address()


@pytest.fixture(scope='function')
def delete_subscribes(driver):
    print('Adding new subscribes')
    yield
    cabinet = PersonalCabinetPage(driver)
    cabinet.uncheck_regular_mailing()
    cabinet.save_subscribes()






