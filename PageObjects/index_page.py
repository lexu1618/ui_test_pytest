import logging
import time
from Common.basepage import BasePage
from Common.handler_log import logger
from PageObjects.person_setting_page import PersonSettingPage


class IndexPage(BasePage):
    _logout = ('xpath', '//a[text()=" 退出"]')
    _person_setting = ('xpath', '//a[text()=" 个人"]')

    # 判断退出元素是否存在
    def isExist_logout_ele(self):
        try:
            self.wait_eleVisible(self._logout)
            logging.info("退出元素存在")
            return True
        except:
            return False

    def into_setting(self):
        """
        进入我的账户
        返回我的账户页面
        """
        self.click_element(self._person_setting)
        frames = self.driver.find_elements_by_tag_name("iframe")
        self.switch_iframe(frames[1])
        # time.sleep(1)
        # frames = self.driver.find_elements_by_tag_name("iframe")
        # self.driver.switch_to.frame(frames[1])

        return PersonSettingPage(self.driver)

    # def into_update_password(self):
    #     # 移动到管理员图标
    #     self.move_to_admin()
    #     # 点击修改密码
    #     self.click_update_pwd()
    #     # 切换frame
    #     self.switch_iframe('layui-layer-iframe1')
    #
    # def update_password(self,old_pwd,pwd):
    #     #输入密码
    #
    #     self.input_text(iloc.old_pwd_button,old_pwd)
    #     self.input_text(iloc.new_pwd_button,pwd)
    #     self.input_text(iloc.new_pwd_confirm_button,pwd)
    #     #切换回默认frame
    #     self.back_defaultFrame()
    #     #点击确定
    #     self.click_element(iloc.pwd_confirm)
    #     return self
    #
    # def logout(self):
    #     self.move_to_admin()
    #     self.click_logout()
    #     return self
    #
    #
    #
    # def move_to_admin(self):
    #     return self.move_to_ele(iloc.Administrator_button)
    #
    # def click_update_pwd(self):
    #     return self.click_element(iloc.update_pwd_button)
    #
    # def click_personal_center(self):
    #     return self.click_element(iloc.my_account_button)
    #
    # def click_logout(self):
    #     return self.click_element(iloc.logout_button)
    #
    #
    #
    # def switch_realMNData(self):
    #     self.click_element(iloc.real_data_button)
    #     self.click_element(iloc.MN_button)
    #     return self
    #
    # def switch_realKGData(self):
    #     self.click_element(iloc.real_data_button)
    #     self.click_element(iloc.KG_button)
    #     return self


if __name__ == '__main__':
    pass
