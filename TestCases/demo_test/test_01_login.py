import pytest
import allure
import time

from Common.handler_log import logger
from Common.handle_yaml import HandleYaml
from Common.dir_config import *
from Common.basepage import BasePage
from PageObjects.login_page import LoginPage



login_data = HandleYaml.read_alone(login_data_dir)
login_success_data = login_data["success_data"]
emptyUser_data = login_data["emptyUser_data"]
emptyPwd_data = login_data["emptyPwd_data"]
emptyVerify_data = login_data["emptyVerify_data"]
errorVerify_data = login_data["errorVerify_data"]
errorLogin_data = login_data["errorLogin_data"]



@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单功能测试")
@allure.feature("登录模块")
@pytest.mark.usefixtures("refresh_web")
@allure.suite("套件1")
class TestLogin():


    @allure.story("测试用例：登录")
    @allure.title("异常登录--用户名不输")
    @allure.description("不输入用户名登录")
    @allure.testcase("http://120.78.128.25:8765/Index/login.html")
    @pytest.mark.parametrize("user,pwd,verify,expect",emptyUser_data)
    def test_login_emptyUser(self,user,pwd,verify,expect,driver):
        logger.info("************************* 开始执行用例 **********************************")
        login_page = LoginPage(driver)
        with allure.step("step1：不输入用户名，输入密码，验证码登录"):
            login_page.login_exception(user,pwd,verify)

        with allure.step("step2：验证提示信息与期望值是否一致"):
            try:
                assert expect in login_page.get_errorUser_login(),"断言失败"
            except AssertionError as e:
                logger.info("测试用例：{}--{}-{}-{}, 失败：{}".format(self.test_login_emptyUser.__name__,\
                                                               user,pwd,verify,expect,e))
                login_page.save_screenshot('login_fail')
                raise e
            else:
                logger.info("测试用例{}-{}-{}测试通过".format(
                    self.test_login_emptyUser.__name__, \
                    user, pwd, verify,expect))
                logger.info("=================结束断言,进入下一个测试用例==================")



    @allure.story("测试用例：登录")
    @allure.title("异常登录--密码不输")
    @allure.description("不输入密码登录")
    @allure.testcase("http://120.78.128.25:8765/Index/login.html")
    @pytest.mark.parametrize("user,pwd,,verify,expect",emptyPwd_data)
    def test_login_emptyPwd(self,user,pwd,verify,expect,driver):
        logger.info("************************* 开始执行用例 **********************************")
        login_page = LoginPage(driver)
        with allure.step("step1：输入用户名，不输入密码"):
            login_page.login_exception(user,pwd,verify)

        with allure.step("step2：验证提示信息与期望值是否一致"):
            try:
                assert expect in login_page.get_errorPassword_login(),"断言失败"
            except AssertionError as e:
                logger.info("测试用例：{}--{}-{}-{}, 失败：{}".format(self.test_login_emptyPwd.__name__,\
                                                               user,pwd,verify,expect,e))
                login_page.save_screenshot('login_fail')
                raise e
            else:
                logger.info("测试用例{}-{}-{}测试通过".format(
                    self.test_login_emptyPwd.__name__, \
                    user, pwd,verify, expect))
                logger.info("=================结束断言,进入下一个测试用例==================")



    @allure.story("测试用例：登录")
    @allure.title("异常登录--密码不输")
    @allure.description("不输入密码登录")
    @allure.testcase("http://120.78.128.25:8765/Index/login.html")
    @pytest.mark.parametrize("user,pwd,,verify,expect",emptyVerify_data)
    def test_login_emptyVerify(self,user,pwd,verify,expect,driver):
        logger.info("************************* 开始执行用例 **********************************")
        login_page = LoginPage(driver)
        with allure.step("step1：输入用户名，不输入密码"):
            login_page.login_exception(user,pwd,verify)

        with allure.step("step2：验证提示信息与期望值是否一致"):
            try:
                assert expect in login_page.get_emptyVerify_login(),"断言失败"
            except AssertionError as e:
                logger.info("测试用例：{}--{}-{}-{}, 失败：{}".format(self.test_login_emptyVerify.__name__,\
                                                               user,pwd,verify,expect,e))
                login_page.save_screenshot('login_fail')
                raise e
            else:
                logger.info("测试用例{}-{}-{}测试通过".format(
                    self.test_login_emptyVerify.__name__, \
                    user, pwd,verify, expect))
                logger.info("=================结束断言,进入下一个测试用例==================")

    @allure.story("测试用例：登录")
    @allure.title("异常登录--密码不输")
    @allure.description("不输入密码登录")
    @allure.testcase("http://120.78.128.25:8765/Index/login.html")
    @pytest.mark.parametrize("user,pwd,,verify,expect", errorVerify_data)
    def test_login_errorVerify(self, user, pwd, verify, expect, driver):
        logger.info("************************* 开始执行用例 **********************************")
        login_page = LoginPage(driver)
        with allure.step("step1：输入用户名，不输入密码"):
            login_page.login_exception(user, pwd, verify)

        with allure.step("step2：验证提示信息与期望值是否一致"):
            try:
                assert expect in login_page.get_errorVerify_login(), "断言失败"
            except AssertionError as e:
                logger.info("测试用例：{}--{}-{}-{}, 失败：{}".format(self.test_login_errorVerify.__name__, \
                                                              user, pwd, verify, expect, e))
                login_page.save_screenshot('login_fail')
                raise e
            else:
                logger.info("测试用例{}-{}-{}测试通过".format(
                    self.test_login_errorVerify.__name__, \
                    user, pwd, verify, expect))
                logger.info("=================结束断言,进入下一个测试用例==================")


    @allure.story("测试用例：登录")
    @allure.title("异常登录--密码不输")
    @allure.description("不输入密码登录")
    @allure.testcase("http://120.78.128.25:8765/Index/login.html")
    @pytest.mark.parametrize("user,pwd,expect", errorLogin_data)
    def test_login_errorLogin(self, user, pwd, expect, driver):
        logger.info("************************* 开始执行用例 **********************************")
        login_page = LoginPage(driver)
        with allure.step("step1：输入用户名，不输入密码"):
            login_page.login_error(user, pwd)

        with allure.step("step2：验证提示信息与期望值是否一致"):
            try:
                assert expect in login_page.get_error_login(), "断言失败"
            except AssertionError as e:
                logger.info("测试用例：{}--{}-{}-{}, 失败：{}".format(self.test_login_errorLogin.__name__, \
                                                              user, pwd, expect, e))
                login_page.save_screenshot('login_fail')
                raise e
            else:
                logger.info("测试用例{}-{}-{}测试通过".format(
                    self.test_login_errorLogin.__name__, \
                    user, pwd,expect))
                logger.info("=================结束断言,进入下一个测试用例==================")




    @allure.story("测试用例：登录")
    @allure.title("正常登录")
    # @allure.description("用户名：{0}，密码：{1}".format(login_success_data["username"],login_success_data["password"]))
    @allure.testcase("http://120.78.128.25:8765/Index/login.html")
    @pytest.mark.parametrize("user,pwd",login_success_data)
    def test_login_success(self,user,pwd,driver):
        logger.info("************************* 开始执行用例 **********************************")
        # login_page = open_url[0]
        # driver = open_url[1]
        # index_page = open_url[2]
        with allure.step("step1：登录"):
            login_page = LoginPage(driver)
            index_page = login_page.login_success(user,pwd)
            time.sleep(5)
        with allure.step("step2：验证"):
            try:
                assert index_page.isExist_logout_ele(),"断言失败"

            except AssertionError as e:
                logger.info("测试用例：{}--{}-{}, 失败：{}".format(self.test_login_errorPwd.__name__,\
                                                            user,pwd, e))
                login_page.save_screenshot('login_fail')
                raise e
            else:
                logger.info("测试用例{}-{}-{}测试通过".format(
                    self.test_login_success.__name__, \
                    user, pwd))
        logger.info("************************* 结束执行用例 **********************************")
        logger.info("")

if __name__ == '__main__':
    pytest.main(["test_01_login.py","-s","-q"])

