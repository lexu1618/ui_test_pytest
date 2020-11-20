from Common.basepage import BasePage
from Common.dir_config import *
from Common.handler_log import logger
from Common.handler_OCR import Hanlder_Code
from Common.handle_yaml import HandleYaml
from PageObjects.index_page import IndexPage

import urllib3

urllib3.disable_warnings()

class LoginPage(BasePage):


    _username =("name","username")
    _password = ("name","password")
    _login=("id","login")
    _verify_input=("id","verify")
    _verify_picture= ('id',"imgVerify")
    _username_error =('id','username-error')
    _password_error = ('id','password-error')
    _login_error = ('xpath','//div[text()="用户或密码错误"]')
    _verify_error = ('xpath','//div[text()="请输入正确的验证码"]')
    _verify_empty_error = ('xpath','//div[text()="请输入验证码"]')

    url = HandleYaml.read_alone(common_data_dir)["login_url"]

#正常登陆
    def login_success(self,username,password):
        '''
        正常登录步骤
        username 登录用户名
        password 登录密码
        返回首页页面
        '''
        doc = "登陆页面------登陆功能"
        self.open_login_url()
        self.input_user(username)
        self.input_password(password)
        self.input_verify()
        self.click_login()
        return IndexPage(self.driver)

    def login_exception(self, username, password,verify):
        """
        异常登录步骤
        username 登录用户名
        password 登录密码
        返回 self 链式调用：调用登录后继续调用获取预期结果
        """
        self.open_login_url()
        self.input_user(username)
        self.input_password(password)
        # self.input_verify()
        self.input_text(self._verify_input,verify)
        self.click_login()
        return self

    def login_error(self, username, password):
        """
        异常登录步骤
        username 登录用户名
        password 登录密码
        返回 self 链式调用：调用登录后继续调用获取预期结果
        """
        self.open_login_url()
        self.input_user(username)
        self.input_password(password)
        self.input_verify()
        self.click_login()
        return self


    def open_login_url(self):
        self.open(self.url)


    def input_user(self, username : str):
        logger.info("输入用户名:{}".format(username))
        self.clear_input(self._username)
        self.input_text(self._username, text=username)
        return self

    def input_password(self, password: str):
        logger.info("输入密码:{}".format(password))
        self.clear_input(self._password)
        self.input_text(self._password, text=password)
        return self

    '''输入验证码'''
    def input_verify(self):
        self.clear_input(self._verify_input)
        res = Hanlder_Code(self.driver).test_OCR(self._verify_picture)
        '''当验证码识别为None和不足4位数字时重新识别，直到识别出4位数字才去输入 '''
        while res == None or len(res) != 4:
            self.click_element(self._verify_picture)
            res = Hanlder_Code(self.driver).test_OCR(self._verify_picture)
            dig_sum = 0
            if res != None:
                for str in res:
                    # 如果在字符串中有数字，那么字符的数量+1
                    if str.isdigit():
                        print('当前字符是{}'.format(str))
                        dig_sum += 1

                if dig_sum == 4:
                    break
        logger.info("输入验证码:{}".format(res))
        self.input_text(self._verify_input,text=res)
        return self

    def click_login(self):
        logger.info("点击登录按钮")
        self.click_element(self._login)


#获取密码错误提示信息  消失

    def get_error_login(self):
        doc = "登录页面-获取登录错误提示信息"
        try:
            self.wait_eleVisible(self._login_error)
            return self.get_text(self._login_error)
        except :
            return False


#获取错误提示信息

    def get_errorUser_login(self):
        doc = "登录页面-获取登录错误提示信息"
        try:

            self.wait_eleVisible(self._username_error)
            return self.get_text(self._username_error)
        except :
            return False

    # 获取错误提示信息

    def get_errorPassword_login(self):
        doc = "登录页面-获取登录错误提示信息"
        try:

            self.wait_eleVisible(self._password_error)
            return self.get_text(self._password_error)
        except:
            return False

    def get_emptyVerify_login(self):
        doc = "登录页面-获取登录错误提示信息"
        try:

            self.wait_eleVisible(self._verify_empty_error)
            return self.get_text(self._verify_empty_error)
        except:
            return False



    def get_errorVerify_login(self):
        doc = "登录页面-获取登录错误提示信息"
        try:

            self.wait_eleVisible(self._verify_error)
            return self.get_text(self._verify_error)
        except:
            return False


    def isExist_login_button(self):
        try:
            self.wait_eleVisible(self._login)
            logger.info("登录元素存在")
            return True
        except Exception as e:
            logger.info("登录元素不存在")
            return False
            raise e