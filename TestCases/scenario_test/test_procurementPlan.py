from PageObjects.login_page import LoginPage

class TestProcuremnetPlan:


    def test_add_Check(self,driver,testcase_data):

        '''新增采购计划'''
        username = testcase_data["add"]["username"]
        password = testcase_data["add"]["password"]
        title = testcase_data["add"]["title"]
        purchaseTimes = testcase_data["add"]["purchaseTimes"]
        name=testcase_data["add"]["name"]
        model=testcase_data["add"]["model"]
        num=testcase_data["add"]["num"]
        price= testcase_data["add"]["price"]
        brand = testcase_data["add"]["brand"]
        index_page = LoginPage(driver).login_success(username,password)
        buy_plan_page = index_page.into_buyPlan()
        buy_plan_page.into_add()
        buy_plan_page.add_plan(title,purchaseTimes,name,model,num,price,brand)
        # print(buy_plan_page.get_planID())
        index_page.logout()

        '''1级审批'''
        f1_check_username = testcase_data["check1"]["username"]
        f1_check_password = testcase_data["check1"]["password"]
        index_page = LoginPage(driver).login_success(f1_check_username, f1_check_password)
        buy_plan_page = index_page.into_buyPlan()
        buy_plan_page.check_first()
        index_page.logout()

        '''2级审批'''
        f2_check_username = testcase_data["check2"]["username"]
        f2_check_password = testcase_data["check2"]["password"]
        index_page = LoginPage(driver).login_success(f2_check_username, f2_check_password)
        buy_plan_page = index_page.into_buyPlan()
        buy_plan_page.check_first()
        index_page.logout()

        '''3级审批'''
        f3_check_username = testcase_data["check3"]["username"]
        f3_check_password = testcase_data["check3"]["password"]
        index_page = LoginPage(driver).login_success(f3_check_username, f3_check_password)
        buy_plan_page = index_page.into_buyPlan()
        buy_plan_page.check_first()
        index_page.logout()

