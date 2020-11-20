import pytest
import time

from config.path import *
from selenium import webdriver
from Common.handle_yaml import HandleYaml
from Common.dir_config import *
from PageObjects.login_page import LoginPage




login_url = HandleYaml.read_alone(common_data_dir)["login_url"]
admin_user = HandleYaml.read_alone(common_data_dir)["username"]
admin_password = HandleYaml.read_alone(common_data_dir)["password"]

scenario_data = HandleYaml.read_alone(scenario_data_dir)

@pytest.fixture(scope="class")
def driver():
    ''''''
    # 加启动配置
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

    driver = webdriver.Chrome(options=chrome_options,executable_path=chromeDrive_path)
                                                            # 此处是我chormedriver放的位置

    yield driver
    #后置条件
    print("所有用例执行后，只执行一次")
    driver.quit()

# @pytest.fixture(scope='module')
# def ini_pages(driver):
#     '''实例化所有页面'''
#     login_page = LoginPage(driver)
#     index_page = IndexPage(driver)
#     user_page = UserPage(driver)
#     yield driver, login_page, index_page,user_page


@pytest.fixture(autouse=True)
def refresh_web(driver):
    '''刷新页面'''
    yield
    driver.refresh()


@pytest.fixture(scope='class',autouse=False)
def login(driver):
    """
    正常登录
    返回成功登录后首页
    """
    login_page =LoginPage(driver)
    indexPage = login_page.login_success(admin_user,admin_password)
    return indexPage







# @pytest.fixture(scope="module")
# def open_url(ini_pages):
#     '''加载网页'''
#     driver = ini_pages[0]
#     login_page = ini_pages[1]
#     index_page = ini_pages[2]
#     login_page.open_login_url()
#     yield login_page,driver,index_page
#     driver.delete_all_cookies()


@pytest.fixture(scope="class")
def get_cookie(driver):
    '''获取cookie里JESSION的值'''

    cookie = driver.get_cookies()["value"]
    return cookie


@pytest.fixture(scope="session",autouse=True)
def clean_driver():
    yield
    os.system('taskkill /iM Chrome.exe /F')


@pytest.fixture()
def update_pwd(login):
    index_page = login[0]
    driver = login[2]
    index_page.move_to_admin()
    index_page.into_update_password()


if __name__ == '__main__':
    login()

