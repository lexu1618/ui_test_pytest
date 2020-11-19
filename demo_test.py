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

try:
    driver.find_element_by_xpath('//a[text()=" 个人"]').click()
    sleep(1)

    frames = driver.find_elements_by_tag_name("iframe")
    driver.switch_to.frame(frames[1])

    driver.find_element_by_xpath('//a[text()="基本资料"]').click()
    sleep(1)
    driver.find_element_by_id("userName").clear()
    driver.find_element_by_id("userName").send_keys("狗蛋")

    driver.find_elements_by_css_selector(".iCheck-helper")[0].click()
    js_value = 'document.getElementById("birth").value="2016-12-25"'
    driver.execute_script(js_value)

    #选择框
    # s1 = driver.find_element_by_id("province")
    # Select(s1).select_by_index(3)
    # s2 =driver.find_element_by_id("city")
    # Select(s2).select_by_index(2)
    # s3 = driver.find_element_by_id("district")
    # Select(s3).select_by_index(2)

    select = driver.find_element_by_name("province")
    # 获取select选项元素集
    elements = select.find_elements_by_xpath("//option")
    # 把select元素集的内容放到一个列表中
    list = []
    for element in elements:
        s = element.text
        list.append(s)
    # 通过列表的index方法定位到传进来的内容是第几个元素再进行点击选择
    print(list)
    num = random.choice(list[1:])
    print(num)
    elements[list.index(num)].click()


    driver.find_elements_by_css_selector(".iCheck-helper")[random.randint(2,4)].click()
    sleep(2)

    #滑动到指定元素可见位置
    target = driver.find_element_by_id("base_save")
    driver.execute_script("arguments[0].scrollIntoView();", target)
    target.click()
    # js = 'var action=document.documentElement.scrollTop=10000'
    # # 设置滚动条距离顶部的位置，设置为 10000， 超过10000就是最底部
    # driver.execute_script(js)  # 执行脚本
    sleep(1)
    driver.switch_to.default_content()
    ele = WebDriverWait(driver,10,0.3).until(EC.visibility_of_element_located(("xpath","//div[text()='更新成功']")))
    print(ele.text)
    # #关闭窗口
    driver.switch_to.default_content()
    # driver.find_elements_by_css_selector("span.layui-layer-setwin>a")[2].click()

except Exception as e:
    raise e