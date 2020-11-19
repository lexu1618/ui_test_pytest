import random
from Common.basepage import BasePage
from Common.dir_config import *
from Common.handler_log import logger
from Common.handler_OCR import Hanlder_Code
from Common.handle_yaml import HandleYaml
from Common.handler_ini import Handle_ini




class PersonSettingPage(BasePage):
    '''基本资料'''
    _baseData = ("xpath",'//a[text()="基本资料"]')
    '''修改头像'''
    _updateHead = ("xpath","//a[text()=头像修改']")
    '''修改密码'''
    _updatePwd = ("xpath","//a[text()=修改密码']")
    '''姓名'''
    _name =('id',"userName")
    '''性别男'''
    _sexMan = ('xpath','//input[@value="96"]')
    '''性别女'''
    _sexWoman = ('xpath', '//input[@value="97"]')
    '''出生年月'''
    _birthday ="birth"
    '''手机号码'''
    _phone = ('id',"phone")
    '''邮箱'''
    _email=("id","email")
    '''省份'''
    _province=("id","province")
    '''城市'''
    _city = ("id","city")
    '''地区'''
    _district = ("id","district")
    '''联系地址'''
    _address = ("id","address")
    '''爱好：看电影'''
    _movie = ("css selector",".iCheck-helper")
    '''爱好：绘画'''
    _movie = ("css selector", ".iCheck-helper")
    '''保存'''
    _save = ("id","base_save")
    '''爱好：编码'''
    _movie = ("css selector", ".iCheck-helper")
    '''旧密码'''
    _pwdOld = ("id","pwdOld")
    '''新密码'''
    _pwdNew=("id","pwdNew")
    '''确认密码'''
    _pwdConfirm = ("id","confirm_password")
    '''更新成功'''
    _update_prompt=("xpath","//div[text()='更新成功']")

    '''更新个人资料'''
    def update_base_data_success(self,name,sex,birth,phone,email,province,city,district,address):
        self.click_element(self._baseData)
        self.input_name(name)
        self.input_sex(sex)
        self.input_birth(birth)
        self.input_phone(phone)
        self.input_email(email)
        self.input_location(province,city,district)
        self.input_address(address)
        self.scrool_to_loc(self._save)
        self.click_element(self._save)



    '''判断更新成功提示是否存在'''
    def isExist_update_prompt(self):
        try:
            self.back_defaultFrame()
            self.wait_eleVisible(self._update_prompt)
            logger.info("更新成功存在")
            return True
        except:
            logger.info("更新成功不存在")
            return False



    def input_name(self,name):
        #清空
        self.clear_input(self._name)
        #输入
        self.input_text(self._name,name)

    def input_sex(self,sex):
        if sex == "男":
            self.click_element(self._sexMan)
        else:
            self.click_element(self._sexWoman)

    def input_birth(self,birth):
        js_value = 'document.getElementById("birth").value={}'.format(birth)
        self.driver.execute_script(js_value)

    def input_phone(self,phone):
        self.clear_input(self._phone)
        self.input_text(self._phone,phone)

    def input_email(self,email):
        self.clear_input(self._email)
        self.input_text(self._email,email)

    '''居住地选择'''
    def input_location(self,province,city,district):
        # select = self.get_element(self._province)
        # # 获取select选项元素集
        # elements = select.find_elements_by_xpath("//option")
        # # 把select元素集的内容放到一个列表中
        # list = []
        # for element in elements:
        #     s = element.text
        #     list.append(s)
        # # 通过列表的index方法定位到传进来的内容是第几个元素再进行点击选择
        # print(list)
        # num = random.choice(list[1:])
        # print(num)
        # elements[list.index(num)].click()
        self.doSelect(self._province,province)
        self.doSelect(self._city,city)
        self.doSelect(self._district,district)


    def input_address(self,address):
        self.clear_input(self._address)
        self.input_text(self._address,address)




