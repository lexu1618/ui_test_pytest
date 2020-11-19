from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://172.16.20.25:8099/login")
driver.maximize_window()
time.sleep(1)
driver.find_element_by_id("txtUserName").send_keys("admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("login_submit").click()

time.sleep(2)
# cookies = driver.get_cookies()
# print(cookies)
# for cookie in cookies:
#     print(cookie)
# #点击实时数据
# driver.find_element_by_xpath('//*[@id="side-menu"]/li[3]/a/span[1]').click()
#
# time.sleep(1)
# #点击模拟量
# driver.find_element_by_xpath('//*[@id="side-menu"]/li[3]/ul/li[1]/a').click()
#
# time.sleep(1)
# #切换到iframe
# driver.switch_to.frame('iframe1')
# time.sleep(1)
# #点击查询
# driver.find_element_by_xpath('//i[@class="fa fa-search"]').click()
# time.sleep(1)
# driver.switch_to.default_content()

# driver.find_element_by_xpath('//*[@id="side-menu"]/li[4]/ul/li[2]/a').click()
# totalEle = driver.find_element_by_xpath('//span[@class="pagination-info"]')
# print(totalEle.text)

ele = driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[1]/nav/ul/li[2]/a/span')
ActionChains(driver).move_to_element(ele).perform()
time.sleep(1)
driver.find_element_by_link_text(u"修改密码").click()
time.sleep(3)
# driver.switch_to.frame('iframe0')
# time.sleep(1)
# frame_ele = driver.find_element_by_xpath('/html/body/div[4]/div[2]/iframe')
# time.sleep(1)
# print(frame_ele)
# driver.switch_to.frame(frame_ele)

# driver.find_element_by_id("oldPassword").send_keys("1123")


# frame_ele = driver.find_element_by_xpath('/html/body/div[4]/div[2]/iframe')
# driver.switch_to.frame(frame_ele)
# driver.find_element_by_id("oldPassword").send_keys("1123")

ele = driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[1]')
print(ele.text)

driver.switch_to.frame('layui-layer-iframe1')
driver.find_element_by_id('oldPassword').send_keys('112121')
driver.switch_to.default_content()
driver.find_element_by_link_text("确定").click()