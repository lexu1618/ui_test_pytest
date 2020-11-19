#  1、封装基本函数   --执行日志   异常处理   失败截图
#  2、所有页面的公共行为

import time
import datetime
from config.path import *
from Common.handler_log import logger

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Common.dir_config import *
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import (NoSuchElementException,
                                        TimeoutException,
                                        NoAlertPresentException,
                                        InvalidArgumentException)

class BasePage:

    def __init__(self,driver:webdriver):

        self.driver = driver
        self.base_url = "http://106.12.13.216:42016"

    # def startBrowser(name):
    #     """
    #     打开浏览器函数，"firefox"、"chrome"、"ie"、"phantomjs"
    #     """
    #     try:
    #         if name == "firefox" or name == "Firefox" or name == "ff":
    #             print("start browser name :Firefox")
    #             driver = webdriver.Firefox()
    #             return driver
    #         elif name == "chrome" or name == "Chrome":
    #             print("start browser name :Chrome")
    #             driver = webdriver.Chrome()
    #             return driver
    #         elif name == "ie" or name == "Ie":
    #             print("start browser name :Ie")
    #             driver = webdriver.Ie()
    #             return driver
    #         elif name == "phantomjs" or name == "Phantomjs":
    #             print("start browser name :phantomjs")
    #             driver = webdriver.PhantomJS()
    #             return driver
    #         else:
    #             print("Not found this browser,You can use 'firefox', 'chrome', 'ie' or 'phantomjs'")
    #     except Exception as msg:
    #         print("启动浏览器出现异常：%s" % str(msg))



    def open(self, url=None):
        try:
            url = url or self.base_url
            self.driver.get(url)
            self.driver.maximize_window()
        except InvalidArgumentException as e:
            logger.error('加载测试地址{}失败:{}'.format(url, e))
            self.save_screenshot("url")
            raise e
        else:
            logger.info('加载测试地址:{}'.format(url))


    #等待元素可见
    def wait_eleVisible(self,locator:tuple, timeout=20, poll_frequency=0.5,doc = '')-> WebElement:
        '''

        :param locator: 元素定位，元祖形式（定位类型，定位方式）  (By.XPATH," xxxxxxx")
        :param timeout:
        :param poll_frequency:
        :param doc: 模块名_页面名称_操作名称   这里只是一个说明截图的用处
        :return:
        '''
        logger.info("等待元素{0}可见".format(locator))
        try:
            #开始等待的时间
            start = datetime.datetime.now()
            ele = WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_time = (end-start).seconds
            logger.info("{0}：元素{1}可见，等待起始时间：{2}，等待结束时间{3}，等待时长：{4}".format(doc,locator,start,end,wait_time))

        except (NoSuchElementException,TimeoutException) as e:
            logger.error("{0} 秒内页面{1}中不存在元素：{2}！！！！".format(timeout,doc,locator))
            #截图
            self.save_screenshot(doc)
            raise e

    #等待元素存在
    def wait_elePresence(self,locator:tuple,timeout = 20,doc='') -> WebElement:
        logger.info("等待元素{0}可见".format(locator))
        try:
            #开始等待的时间
            start = datetime.datetime.now()
            ele = WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
            end = datetime.datetime.now()
            wait_time = (end-start).seconds
            logger.info("{0}：元素{1}可见，等待起始时间：{2}，等待结束时间{3}，等待时长：{4}".format(doc,locator,start,end,wait_time))

        except (NoSuchElementException,TimeoutException) as e:
            logger.error("{0} 秒内页面{1}中不存在元素：{2}！！！！！".format(timeout,doc,locator))
            #截图
            self.save_screenshot(doc)
            raise e

    #查找元素
    def get_element(self,locator:tuple,doc='')-> WebElement:
        logger.info("查找元素{}".format(doc,locator))

        try:
            self.wait_elePresence(locator)
            return self.driver.find_element(*locator)
        except NoSuchElementException as e:
            logger.error("查找元素失败！！！！！")
            self.save_screenshot(doc)
            raise e

    #
    def get_elements(self,locator:tuple,position=0,doc='')-> WebElement:

        logger.info("查找元素{}".format(doc,locator))
        try:
            self.wait_elePresence(locator)
            return self.driver.find_elements(*locator)[position]
        except:
            logger.error("查找元素失败！！！！！")
            self.save_screenshot(doc)
            raise

    def checkEleEnable(self,locator:tuple,doc='')->bool:
        doc = "判断元素是否可以操作"
        logger.info(doc)
        try:
            ele = self.get_element(locator,doc)
            return ele.is_enabled()
        except:
            logger.error("判断元素是否可以操作失败！！！！！")
            self.save_screenshot(doc)
            raise



    #点击操作
    def click_element(self,locator:tuple,doc=''):
        #找元素
        ele = self.get_element(locator,doc)
        #元素操作
        logger.info("{0}页面:点击元素：{1}".format(doc,locator))

        try:
            ele.click()
            return self
        except Exception as e:
            logger.error("元素点击失败")
            self.save_screenshot(doc)
            raise e

    def doubleClick(self,locator:tuple,doc):
        # 找元素
        ele = self.get_element(locator, doc)
        # 元素操作
        logger.info("{0}页面:点击元素：{1}".format(doc, locator))

        try:
            ActionChains(self.driver).double_click(ele).perform()
            return self
        except:
            logger.error("元素双击失败")
            self.save_screenshot(doc)
            raise

    #输入操作
    def input_text(self,locator:tuple,text,doc=''):
        #找元素
        ele = self.get_element(locator,doc)
        #输入操作
        logger.info("{0} 输入元素：{1}".format(doc,locator))
        try:
            ele.send_keys(text)
            return self
        except:
            logger.info("元素输入失败！！！！！")
            self.save_screenshot(doc)
            raise

    def clear_input(self,locator:tuple,doc= ''):
        '''清除输入内容'''
        doc = '清除输入内容'
        ele = self.get_element(locator,doc)
        #输入操作
        logger.info("{} 清除输入内容{}".format(locator,doc))
        try:
            ele.clear()
            return self
        except:
            logger.info("元素文本清除失败！！！！！")
            self.save_screenshot(doc)
            raise

    def move_to_ele(self,locator:tuple,doc=''):
        '''鼠标移动到某个元素上'''
        doc='鼠标移动到某个元素上'
        ele = self.get_element(locator)
        try:
            ActionChains(self.driver).move_to_element(ele).perform()
            logger.info("鼠标移动到元素{}上".format(doc))
        except Exception as e:
            logger.info("鼠标移动到元素失败！！！")
            raise e

    def back(self,doc= ''):
        '''返回上一页'''
        doc = '返回上一页'
        logger.info("返回上一页")
        try:
            self.driver.back()
            return self
        except:
            logger.info("返回上一页失败！！！！！")
            self.save_screenshot(doc)
            raise

    def refresh(self,doc= ''):

        doc = "刷新当前页面"
        logger.info("刷新当前页面")
        try:
            self.driver.refresh()
            return self
        except:
            logger.info("刷新当前页面！！！！！")
            self.save_screenshot(doc)
            raise

    def forward(self,doc= ''):

        doc = "回到前一页"
        logger.info("回到前一页")
        try:
            self.driver.forward()
            return self
        except:
            logger.info("回到前一页！！！！！")
            self.save_screenshot(doc)
            raise

    def get_window_size(self,doc='',handle='current' ):
        doc = "获取窗口尺寸"
        logger.info("获取窗口尺寸")
        try:
            window_size = self.driver.get_window_size(handle)
            height = window_size["height"]
            width = window_size["width"]
            logger.info("当前窗口的长为{}，宽为{}".format(height,width))
            return height,width
        except:
            logger.info("获取窗口尺寸失败！！！！！")
            self.save_screenshot(doc)
            raise


    def set_window_size(self,width, height, windowHandle='current'):
        doc = "设置窗口尺寸"
        logger.info("设置窗口尺寸")
        try:
            self.driver.set_window_size(width,height,windowHandle)
            return self
        except:
            logger.info("设置窗口尺寸失败！！！！！")
            self.save_screenshot(doc)
            raise

    def get_title(self):
        doc = "获取网页title"
        logger.info("获取网页title")
        try:
            return self.driver.title
        except:
            logger.info("获取网页title失败！！！！！")
            self.save_screenshot(doc)
            raise

    def get_cookie(self):
        '''
        获取页面cookie信息
        :return:返回cookies
        '''
        logger.info("获取cookie信息：{0}".format(self.driver.get_cookies()))
        return self.driver.get_cookies()

    def add_cookie(self, **kwargs):
        '''
        添加cookie信息，以字典方式传入
        :param kwargs: 要添加的cookie信息
        :return:
        '''
        logger.info("添加cookie:{0}".format(kwargs))
        self.driver.add_cookie(kwargs)


    def del_cookie(self, name):
        '''
        删除cookie信息，传入cookie名称即可
        :param kwargs: 要删除的cookie信息
        :return:
        '''
        logger.info("删除cookie:{0}".format(name))
        self.driver.delete_cookie(name)


    def get_attribute(self, locator, name,doc='') ->str:
        """获取某元素某属性"""
        attribute = self.wait_eleVisible(locator=locator).get_attribute(name=name)
        return attribute


    #获取元素文本内容
    def get_text(self,locator:tuple,doc='') ->str:
        #找元素
        ele = self.get_element(locator,doc)
        logger.info("{0} 获取元素文本：{1}".format(doc,locator))
        try:
            logger.info(ele.text)
            return ele.text
        except:
            logger.error("获取元素文本失败！！！！！")
            self.save_screenshot(doc)
            raise

    #获取元素文本内容
    def get_texts(self,locator:tuple,position=0,doc='') ->str:
        #找元素

        ele = self.get_elements(locator,position,doc)
        logger.info("{0} 获取元素文本：{1}".format(doc,locator))
        try:
            return  ele.text
        except:
            logger.error("获取元素文本失败！！！！！")
            self.save_screenshot(doc)
            raise




    #获取元素属性
    def get_element_attribute(self,locator :tuple,attr,doc= ''):
        ele = self.get_element(locator,doc)
        try:
            return ele.get_attribute(attr)
        except:
            logger.error("获取元素属性失败！！！！！")
            self.save_screenshot(doc)
            raise


    #alert处理
    def alert_action(self,type =None,action="accept",content=None,doc=''):
        '''
        alert弹窗是F12中无法定位元素的窗口，分为alert  confirm prompt对话框
        alert 是只有确定按钮的窗口，confirm是有确定和取消按钮的窗口，prompt是带有文字输入框的窗口
        :param type:alert  confirm prompt
        :param action:
        :return:
        '''
        doc = "处理弹窗"
        logger.info("处理弹窗")
        try:
            ele = self.driver.switch_to.alert
            text = ele.text
            if type == "alert" and action == "accept":
                ele.accept()
                return text

            elif type == "confirm":
                if action == "accept":
                    ele.accept()
                elif action == "dismiss":
                    ele.dismiss()
                return text
            elif type == "prompt":
                if action == "accept":
                    ele.accept()
                elif action == "dismiss":
                    ele.dismiss()
                elif action == "send_keys":
                    ele.send_keys(content)
                return text

            else:
                logger.info("输入弹窗类型错误")
                return False
        except:
            logger.error("处理弹窗失败！！！！！")
            self.save_screenshot(doc)
            raise

    #获取当前窗口句柄
    def getWindowHandle(self,doc=''):
        doc = "获取当前窗口句柄"
        logger.info("获取当前窗口句柄")
        try:
            return self.driver.current_window_handle
        except:
            logger.info("获取当前窗口句柄失败！！！")
            self.save_screenshot(doc)
            raise

    #句柄切换  (不确定)
    def tab_handle(self,doc=''):
        doc = "切换句柄"
        logger.info("切换句柄")
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != self.getWindowHandle():
                self.driver.switch_to.window(handle)


    def input_select(self,locator:tuple,doc,text,action=None,count=None):
        '''
        输入框联想内容输入
        :param locator:
        :param doc:
        :param text:  输入的内容
        :param action:  Keys.ARROW_DOWN   Keys.ARROW_UP
        :param time: 次数
        :return:
        '''
        doc = 'input类型选择框'
        logger.info(doc)
        #找到选择框元素
        selectEle = self.get_element(locator,doc)
        #清空输入选择框内容
        self.clear_input(selectEle)
        #输入内容 按下键盘上下选择
        selectEle.send_keys(text)
        if action and count != None:
            for i in range(count):
                time.sleep(1)
                selectEle.send_keys(action)
        return self



    def doSelect(self,locatorSelect:str,text,doc=''):
        '''
        :param locatorSelect: select选择框的定位元素
        :param text: 选项值
        :param doc:
        :return:
        '''
        # 定位到select元素
        select = self.get_element(locatorSelect)
        #获取select选项元素集
        elements =select.find_elements_by_xpath("//option")
        #把select元素集的内容放到一个列表中
        list = []
        for element in elements:
            s = element.text
            list.append(s)
        # 通过列表的index方法定位到传进来的内容是第几个元素再进行点击选择
        elements[list.index(text)].click()


    def get_selectOption(self,locator:tuple,doc):
        from selenium.webdriver.support.ui import Select
        select_element = Select(self.get_element(locator))
        # 打印默认选项
        print(select_element.first_selected_option.text)
        # 获取所有下拉选项元素
        all_options = select_element.options
        # 打印下拉选项的个数
        print(len(all_options))
        # 如果第二个选项可以操作且没有被选中，那么我们就选择这个选项
        if all_options[1].is_enabled() and not all_options[1].is_selected():
            # 第一个方法 通过序号选择选项 序号从0开始
            select_element.select_by_index(1)
            # 打印选中选项的文本
            print(select_element.all_selected_options[0].text)
        time.sleep(2)




    def getMultipleOptions(self,locator:tuple,doc):
        '''
        一个可以多选的列表形式选择框
        :param locator:
        :param doc:
        :return:
        '''
        from selenium.webdriver.support.ui import Select
        select_element = Select(self.get_element(locator))
        # 通过序号选择第一个元素
        select_element.select_by_index(0)
        # 通过文本选择山楂
        select_element.select_by_visible_text('山楂')
        # 通过选项的value属性值选择value=猕猴桃
        select_element.select_by_value('nihoutao')
        # 打印所有选中文本
        for option in select_element.all_selected_options:
            print(option.text)
            # 再次选中3个选项
        select_element.select_by_index(1)
        select_element.select_by_value('juzi')
        select_element.select_by_visible_text('荔枝')
        # 取消3个选项
        select_element.deselect_by_index(0)
        select_element.deselect_by_value('nihoutao')
        select_element.deselect_by_visible_text('山楂')

    def selectRadio(self,locator,doc):
        '''
        Radio 就是一组互斥的通过圆点的选择项

        :param locator:
        :param doc:
        :return:
        '''
        time.sleep(2)
        ele = self.get_element(locator)
        self.click_element(ele)
        # 断言是否被选中
        # self.assertTrue(berry.is_selected())

    def selectCheckBox(self,locator:tuple,doc):
        ele = self.get_element(locator)
        self.click_element(ele)
        #取消选中
        if ele.is_selected():
            self.click_element(ele)


    #上传操作
    def upload_file(self):
        pass

    #滚动条处理
    def execute_window_scroll(self, x: str, y: str):
        """滚动窗口"""
        try:
            js = 'window.scrollTo(' + x + ',' + y + ')'
            self.driver.execute_script(js)
        except InvalidArgumentException as e:
            self.logger.error("执行JS脚本失败{}".format(e))
            raise e

    # switch_to.active_element
    # switch_to.active_element返回的是当前焦点的对象，即返回WebElement对象。
    #
    # 那么焦点是什么？大概可以这样理解：即网页上当前操作的对象（也就是你网页上光标的位置），比如，你鼠标点击到了一个input框，你可以在这个input框里输入信息，这时这个input框即焦点。

    '''滚动条滑动到元素可见位置'''
    def scrool_to_loc(self,locator:tuple,doc=''):
        doc = "滑动到元素：{}".format(locator)
        target = self.get_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)
        logger.info(doc)


    #窗口切换

    #iframe切换
    def switch_iframe(self,iframe_refrence):
        '''

        :param iframe_refrence:  可以是index，id，name 定位frame
        :return:
        '''
        time.sleep(2)
        self.driver.switch_to.frame(iframe_refrence)
        logger.info("切换到frame:{}".format(iframe_refrence))
        return self

    '''释放frame'''
    def back_defaultFrame(self):
        return self.driver.switch_to.default_content()



    #截图    只截图浏览器网页的内容，上传窗口也无法截到
    def save_screenshot(self,name:str,doc=''):
        #图片名称： 模块名_页面名称_操作名称_时间.png
        currentDate = time.strftime("%Y-%m-%d")
        currentTime = time.strftime("%H-%M-%S")
        # dateDir = os.path.join(screenShot_path,currentDate)
        # if not os.path.exists(dateDir):
        #     os.mkdir(dateDir)
        #
        # # file_name =name+ "  " + currentTime +".png"     #文件名不能有冒号，空格，否则截图不会生成
        file_name = name +".png"


        file_dir = os.path.join(screenShot_path,file_name)
        try:
            self.driver.save_screenshot(file_dir)
            return self
            logger.info("截图成功，文件路径为{}".format(file_dir))
        except:
            logger.error("截图失败")
