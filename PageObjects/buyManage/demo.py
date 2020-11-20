import random
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.handler_OCR import Hanlder_Code
from time import sleep

driver = webdriver.Chrome()
driver.get("http://106.12.13.216:42016/login")
driver.maximize_window()
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("111111")
driver.find_element_by_id("verify").clear()

res = Hanlder_Code(driver).test_OCR(('id',"imgVerify"))
'''当验证码识别为None和不足4位数字时重新识别，直到识别出4位数字才去输入 '''
while res == None or len(res) != 4:
    driver.find_element_by_id("imgVerify").click()
    res = Hanlder_Code(driver).test_OCR(('id',"imgVerify"))
    dig_sum = 0
    if res != None:
        for strs in res:
            # 如果在字符串中有数字，那么字符的数量+1
            if strs.isdigit():
                print('当前字符是{}'.format(strs))
                dig_sum += 1

        if dig_sum == 4:
            break

driver.find_element_by_id("verify").send_keys(res)
driver.find_element_by_id("login").click()

sleep(2)
driver.find_element_by_xpath("//span[text()='购置管理']").click()
sleep(1)
driver.find_element_by_css_selector("#side-menu > li.active > ul > li:nth-child(1) > a").click()

frames = driver.find_elements_by_tag_name("iframe")
print(frames)
driver.switch_to.frame(frames[1])


'''切换到内嵌frame'''
frames2 = driver.find_elements_by_tag_name("iframe")
print(frames2)
driver.switch_to.frame(frames2[0])
sleep(1)
driver.find_element_by_css_selector("div.columns.pull-right > button.btn.btn-primary").click()

frames3 = driver.find_elements_by_tag_name("iframe")
driver.switch_to.frame(frames3[0])

sleep(1)
driver.find_element_by_css_selector("#title").send_keys("采购计划9998")

# eles = driver.find_elements_by_id("type")
# Select(eles[0]).select_by_index(1)

eles = driver.find_elements_by_id("type_chosen")
eles[0].click()
driver.find_element_by_xpath('//li[text()="设备采购"]').click()

driver.find_element_by_id("purchaseTimes").send_keys("2")

driver.find_elements_by_id("purchaseTimesType_chosen")[0].click()

driver.find_element_by_xpath('//li[text()="月"]').click()

driver.find_elements_by_css_selector("button.layui-btn.layui-btn-normal.layui-btn-sm")[0].click()

driver.find_element_by_css_selector("[name='name']").send_keys("设备1")

driver.find_element_by_css_selector("[name='specification']").send_keys("无")


driver.find_element_by_css_selector("[name='num']").send_keys("2")

driver.find_element_by_css_selector("[name='price']").send_keys("10")

driver.find_element_by_css_selector("[name='brand']").send_keys("SB")

upload = driver.find_element_by_css_selector(".layui-upload-file")
upload.send_keys(r"D:\requirements.txt")

driver.find_element_by_css_selector("#submit").click()

