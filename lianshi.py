# class A:
#     def test(self,name):
#         self.name=name
#         return self
#     def test2(self,age):
#         self.age=age
#         return self
# a=A()
# a.test('lqz').test2(19)
# print(a.name)
# print(a.age)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://172.16.20.25:8099/login")
driver.maximize_window()
driver.find_element_by_id("txtUserName").send_keys("admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("login_submit").click()
##报错提示
# ele = WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH, "//div[@class='layui-layer-content']")))
# print(ele.text)
# print(ele.rect)
# print(ele.size)
# print(ele.location)
