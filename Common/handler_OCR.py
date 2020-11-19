import PIL
import requests
import base64
from PIL import Image
from config.path import *
from requests.packages import urllib3
from Common.handler_ini import Handle_ini
from Common.basepage import BasePage

#去除HTTPS控制台警告
urllib3.disable_warnings()


class Hanlder_Code(BasePage):
    OCR_data = Handle_ini(setting_path).get_all_options("OCR")
    def get_token(self):
        token_host = self.OCR_data["TOKEN_URL"] +"?"+"grant_type=client_credentials&client_id=HLaq5GafbfsuXzVIC2mO0Yjr&client_secret=27j73DFMGXjPIu6vhKTCAhlGSuHFYoQ6"
        res = requests.get(token_host, verify=False)
        if res:
            return res.json()["access_token"]

    def getCode_img(self,locator:tuple):
        #打开网页，定位元素
  # 1、获取到验证码的图片
        # 保存整个页面截图
        self.save_screenshot("page")
        # 定位页面中的验证码
        v_code = self.get_element(locator)
        # 获取验证码图片的坐标位置
        size = v_code.size
        loc = v_code.location
        # 获取左边界位置
        left = loc["x"]
        # 获取右边界
        right = (loc['x'] + size["width"])
        # 获取上边界
        top = loc['y']
        # 获取下边界
        bot = (loc['y'] + size["height"])
        # 坐标位置的顺序：左  上   右   下
        location = (left, top, right, bot)
        # 打开页面图片
        page = PIL.Image.open(screenShot_path +"\page.png")
        # 根据坐标位置进行截图
        code_image = screenShot_path+"\code.png"
        page.crop(location).save(code_image)
        print(code_image)
        # 保存截取下来的图片（验证码）
        return code_image

    def read_file(self,image_path):
        f = None
        try:
            f = open(image_path, 'rb')
            return f.read()
        except:
            print('read image file fail')
            return None
        finally:
            if f:
                f.close()

    def requestOcr(self, url,data):
        response = requests.post(url, data,verify=False)
        if response:
            return response

    def test_OCR(self,locator):
        # 获取access token
        token = self.get_token()
        print("token 是{}".format(token))
        print("Ocr_host 是{}".format(self.OCR_data["OCR_URL"]))
        # 拼接通用文字识别高精度url
        image_url = self.OCR_data["OCR_URL"] + "?access_token=" + token
        text = ""
        # 读取验证码图片
        # time.sleep(2)
        imagepath = self.getCode_img(locator)
        print("imagepath是{}".format(imagepath))
        file_content = self.read_file(imagepath)
        # 调用文字识别服务
        result_json = self.requestOcr(image_url,data={'image': base64.b64encode(file_content)}).json()
        print("result是{}".format(result_json))

        # 解析返回结果
        for words_result in result_json["words_result"]:
            text = text + words_result["words"]
            # 打印文字
            # type(r"D:\进阶\1.jpg", text)
            # print(text)
            return text

if __name__ == '__main__':
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

    driver = webdriver.Chrome(options=chrome_options, executable_path=chromeDrive_path)
    # 此处是我chormedriver放的位置

    # OCR_data = Handle_ini(setting_path).get_all_options("OCR")
    # print(OCR_data)

    code = Hanlder_Code(driver)
    driver.get("http://106.12.13.216:42016/login")
    driver.maximize_window()
    time.sleep(2)
    res = code.test_OCR((By.ID,"imgVerify"))
    print("验证码识别是：{}".format(res))

    while res == None or len(res)!=4:
        driver.find_element_by_id("imgVerify").click()
        res = code.test_OCR((By.ID, "imgVerify"))
        if res != None:
            dig_sum = 0
            for strs in res:
                # 如果在字符串中有字符，那么字符的数量+1
                if strs.isdigit():
                    dig_sum += 1

            if dig_sum == 4:
                break

    print(type(res))
    driver.find_element_by_id('verify').send_keys(res)
    driver.find_element_by_id('login').click()
    # driver.quit()

