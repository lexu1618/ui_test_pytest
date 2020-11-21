import pytest
from time import sleep
from Common.handler_log import logger
from PageObjects.login_page import LoginPage


class TestProcuremnetPlan:

    '''新增采购计划-1级审批打回'''
    def test_add_first_disagree(self, driver, testcase_data):
        '''新增采购计划'''
        username = testcase_data["add"]["username"]
        password = testcase_data["add"]["password"]
        title = testcase_data["add"]["title"]
        purchaseTimes = testcase_data["add"]["purchaseTimes"]
        name = testcase_data["add"]["name"]
        model = testcase_data["add"]["model"]
        num = testcase_data["add"]["num"]
        price = testcase_data["add"]["price"]
        brand = testcase_data["add"]["brand"]
        index_page = LoginPage(driver).login_success(username, password)
        buy_plan_page = index_page.into_buyPlan()
        buy_plan_page.into_add()
        buy_plan_page.add_plan(title, purchaseTimes, name, model, num, price, brand)
        planID = buy_plan_page.get_planID()
        print(planID)
        sleep(1)
        index_page.back_defaultFrame()
        index_page.logout()

        '''1级审批'''
        f1_check_username = testcase_data["check1"]["username"]
        f1_check_password = testcase_data["check1"]["password"]
        index_page = LoginPage(driver).login_success(f1_check_username, f1_check_password)
        buy_plan_page = index_page.into_buyPlan()
        buy_plan_page.into_related_to_myself()
        assert "一级审批" in driver.page_source
        buy_plan_page.check_first_disagree()
        index_page.logout()

        '''断言'''
        '''2级审批'''
        f2_check_username = testcase_data["check2"]["username"]
        f2_check_password = testcase_data["check2"]["password"]
        index_page = LoginPage(driver).login_success(f2_check_username, f2_check_password)
        buy_plan_page = index_page.into_buyPlan()
        buy_plan_page.into_related_to_myself()
        assert "二级审批" not in driver.page_source
        driver.switch_to_default_content()
        index_page.logout()

        '''提单账号断言'''
        index_page = LoginPage(driver).login_success(username, password)
        buy_plan_page = index_page.into_buyPlan()
        res = buy_plan_page.get_disagree_check_status()
        print(res)
        assert res in "已打回"
        buy_plan_page.delete_end_plan()



    '''新增采购计划-2级审批打回'''

    def test_add_second_disagree(self, driver, testcase_data):
        '''新增采购计划'''

        username = testcase_data["add"]["username"]
        password = testcase_data["add"]["password"]
        title = testcase_data["add"]["title"]
        purchaseTimes = testcase_data["add"]["purchaseTimes"]
        name = testcase_data["add"]["name"]
        model = testcase_data["add"]["model"]
        num = testcase_data["add"]["num"]
        price = testcase_data["add"]["price"]
        brand = testcase_data["add"]["brand"]
        index_page = LoginPage(driver).login_success(username, password)
        buy_plan_page = index_page.into_buyPlan()
        buy_plan_page.into_add()
        buy_plan_page.add_plan(title, purchaseTimes, name, model, num, price, brand)
        planID = buy_plan_page.get_planID()
        print(planID)
        sleep(1)
        index_page.back_defaultFrame()
        index_page.logout()

        '''1级审批'''
        f1_check_username = testcase_data["check1"]["username"]
        f1_check_password = testcase_data["check1"]["password"]
        index_page = LoginPage(driver).login_success(f1_check_username, f1_check_password)
        buy_plan_page = index_page.into_buyPlan()
        buy_plan_page.into_related_to_myself()
        assert "一级审批" in driver.page_source
        buy_plan_page.check_first_agree()
        index_page.logout()

        '''2级审批'''
        f2_check_username = testcase_data["check2"]["username"]
        f2_check_password = testcase_data["check2"]["password"]
        index_page = LoginPage(driver).login_success(f2_check_username, f2_check_password)
        buy_plan_page = index_page.into_buyPlan()
        buy_plan_page.into_related_to_myself()
        assert "二级审批" in driver.page_source
        buy_plan_page.check_first_disagree()
        index_page.logout()

        '''断言'''
        '''3级审批'''
        f3_check_username = testcase_data["check3"]["username"]
        f3_check_password = testcase_data["check3"]["password"]
        index_page = LoginPage(driver).login_success(f3_check_username, f3_check_password)
        buy_plan_page = index_page.into_buyPlan()
        buy_plan_page.into_related_to_myself()
        assert "末尾审批" not in driver.page_source
        driver.switch_to_default_content()
        index_page.logout()

        '''提单账号断言'''
        index_page = LoginPage(driver).login_success(username, password)
        buy_plan_page = index_page.into_buyPlan()
        res = buy_plan_page.get_disagree_check_status()
        print(res)
        assert res in "已打回"
        buy_plan_page.delete_end_plan()



    '''新增采购计划-1级审批同意-2级审批同意-末级审批同意'''

    def test_add_Check(self, driver, testcase_data):
        try:
            '''新增采购计划'''
            username = testcase_data["add"]["username"]
            password = testcase_data["add"]["password"]
            title = testcase_data["add"]["title"]
            purchaseTimes = testcase_data["add"]["purchaseTimes"]
            name = testcase_data["add"]["name"]
            model = testcase_data["add"]["model"]
            num = testcase_data["add"]["num"]
            price = testcase_data["add"]["price"]
            brand = testcase_data["add"]["brand"]
            index_page = LoginPage(driver).login_success(username, password)
            buy_plan_page = index_page.into_buyPlan()
            buy_plan_page.into_add()
            buy_plan_page.add_plan(title, purchaseTimes, name, model, num, price, brand)
            planID = buy_plan_page.get_planID()
            print(planID)
            sleep(1)
            index_page.back_defaultFrame()
            index_page.logout()

            '''1级审批'''
            f1_check_username = testcase_data["check1"]["username"]
            f1_check_password = testcase_data["check1"]["password"]
            index_page = LoginPage(driver).login_success(f1_check_username, f1_check_password)
            buy_plan_page = index_page.into_buyPlan()
            buy_plan_page.into_related_to_myself()
            assert "一级审批" in driver.page_source
            buy_plan_page.check_first_agree()
            index_page.logout()

            '''2级审批'''

            f2_check_username = testcase_data["check2"]["username"]
            f2_check_password = testcase_data["check2"]["password"]
            index_page = LoginPage(driver).login_success(f2_check_username, f2_check_password)
            buy_plan_page = index_page.into_buyPlan()
            buy_plan_page.into_related_to_myself()
            assert "二级审批" in driver.page_source
            buy_plan_page.check_first_agree()
            index_page.logout()

            '''3级审批'''

            f3_check_username = testcase_data["check3"]["username"]
            f3_check_password = testcase_data["check3"]["password"]
            index_page = LoginPage(driver).login_success(f3_check_username, f3_check_password)
            buy_plan_page = index_page.into_buyPlan()
            buy_plan_page.into_related_to_myself()
            assert "末尾审批" in driver.page_source
            buy_plan_page.check_first_agree()
            index_page.logout()

            '''断言'''
            index_page = LoginPage(driver).login_success(username, password)
            buy_plan_page = index_page.into_buyPlan()
            res = buy_plan_page.select_plan_status(planID)
            print(res)
            assert res in "已结束"
            buy_plan_page.delete_end_plan()
        except Exception as e:
            raise e


if __name__ == '__main__':
    pytest.main(["test_procurementPlan.py"])