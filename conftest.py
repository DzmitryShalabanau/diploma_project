import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOption
from selenium.webdriver.edge.options import Options as EdgeOption
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService


from data import TEST_USER
from elements import HeaderElement
from pages import LoginPage, PersonalCabinetPage, ComparisonPage


def pytest_addoption(parser):
    """
    Adds such options as headless mode of browser and choosing browser type
    """
    parser.addoption('--headless',
                     default='False',
                     help='headless options: "yes" or "no"')
    parser.addoption('--b',
                     default='chrome',
                     help='option to define type of browser')


def create_chrome(headless=True):
    """
    Create Google Chrome browser
    """
    chrome_option = ChromeOption()
    if headless == 'True':
        chrome_option.add_argument('--headless')
        chrome_option.add_argument('window-size=1900x1600')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_option)
    return driver


def create_edge(headless=True):
    """
     Create Microsoft Edge browser
    """
    edge_option = EdgeOption()
    if headless == 'True':
        edge_option.add_argument('--headless')
        edge_option.add_argument('window-size=1900x1600')
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_option)
    return driver


@pytest.fixture(autouse=True)
def driver(request):
    """
    Create browser with chosen options
    """
    driver = None
    browser = request.config.getoption('--b')
    headless = request.config.getoption('--headless')

    print(headless)
    if browser == 'chrome':
        driver = create_chrome(headless)
    if browser == 'edge':
        driver = create_edge(headless)

    driver.implicitly_wait(5)
    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def open_main_page(request):
    """
    Opens www.5element.by
    """
    login = LoginPage(request.node.funcargs['driver'])
    login.open()


@pytest.fixture(autouse=False)
def login(request):
    """
    Logins to www.5element.by as user
    """
    login = LoginPage(request.node.funcargs['driver'])
    login.login(TEST_USER)


@pytest.fixture(scope='function')
def delete_shop(driver):
    """
    Delete favorite shop from personal cabinet
    """
    print('Adding favorite shop')
    yield
    cabinet = PersonalCabinetPage(driver)
    cabinet.delete_favorite_shop()


@pytest.fixture(scope='function')
def delete_address(driver):
    """
    Delete address from personal cabinet
    """
    print('Adding new address')
    yield
    cabinet = PersonalCabinetPage(driver)
    cabinet.click_on_delivery_address()
    cabinet.delete_address()
    cabinet.confirm_delete_address()


@pytest.fixture(scope='function')
def delete_subscribes(driver):
    """
    Delete subscribes from personal cabinet
    """
    print('Adding new subscribes')
    yield
    cabinet = PersonalCabinetPage(driver)
    cabinet.uncheck_regular_mailing()
    cabinet.save_subscribes()
    cabinet.click_on_sub_ok_button()


@pytest.fixture(scope='function')
def add_item_to_comparison(driver):
    """
    Method that adds item to comparison
    """
    header = HeaderElement(driver)
    compare = ComparisonPage(driver)
    header.click_on_search_form()
    header.search_for_item_to_compare()
    compare.add_item_to_comparison()
    compare.move_to_compare_section()


@pytest.fixture(scope='function')
def add_items_to_comparison(driver):
    """
    Method that adds items to comparison
    """
    header = HeaderElement(driver)
    compare = ComparisonPage(driver)
    header.click_on_search_form()
    header.search_for_item_to_compare()
    compare.add_item_to_comparison()
    compare.move_to_compare_section()
    compare.click_on_add_item_button()
    compare.add_second_item_to_comparison()
    compare.move_to_compare_section()
