import pytest
import allure
import time

from Common.handler_log import logger
from Common.handle_yaml import HandleYaml
from Common.dir_config import *

success_data = HandleYaml.read_alone(personData_data_dir)["success_data"]

@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单功能测试")
@allure.feature("个人设置模块")
@pytest.mark.usefixtures("refresh_web")
@allure.suite("套件1")
class TestPersonSetting:
    @allure.story("测试用例：登录")
    @allure.title("异常登录--用户名不输")
    @allure.description("不输入用户名登录")
    @allure.testcase("http://120.78.128.25:8765/Index/login.html")
    @pytest.mark.parametrize("name,sex,birth,phone,email,province,city,district,address",success_data)
    def test_update_baseData_success(self,name,sex,birth,phone,email,province,city,district,address,login):

        logger.info("************************* 开始执行用例 **********************************")
        with allure.step("step1：登录到主页"):
            index_page = login
        with allure.step("step2：点击个人设置，弹出设置框"):
            personsetting_page = index_page.into_setting()
        with allure.step("step3:输入参数，点击提交"):
            personsetting_page.update_base_data_success(name,sex,birth,phone,email,province,city,district,address)
        with allure.step("step4:断言提示框是否存在"):
            try:
                assert personsetting_page.isExist_update_prompt(),"断言失败"
            except AssertionError as e:
                logger.info("测试用例：{}--{}-{}-{}, 失败：{}".format(self.test_update_baseData_success.__name__,\
                                                               name,sex,birth,phone,email,province,city,district,address,e))
                index_page.save_screenshot('login_fail')
                raise e
            else:
                logger.info("测试用例{}-{}-{}测试通过".format(
                    self.test_update_baseData_success.__name__, \
                    name,sex,birth,phone,email,province,city,district,address))

        logger.info("=================结束断言,进入下一个测试用例==================")



if __name__ == '__main__':
    pytest.main(["test_02_person_setting.py","-sv"])