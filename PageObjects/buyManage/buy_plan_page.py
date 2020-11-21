from time import sleep

from Common.basepage import BasePage


class BuyPlanPage(BasePage):
    _add = ("css selector","div.columns.pull-right > button.btn.btn-primary")
    '''get_elements[0]'''
    _select = ("css selector","div.columns.pull-right > button.btn.btn-success")
    '''标题'''
    _title = ("css selector","#title")
    '''采购类型get_elements[0]'''
    _type =("id","type_chosen")
    '''采购类型--设备采购'''
    _type_mechina_buy=("xpath",'//li[text()="设备采购"]')
    '''采购周期'''
    _purchaseTimes = ("id","purchaseTimes")
    '''周期类型'''
    _purchaseTimesTypeChosen=("id","purchaseTimesType_chosen")
    '''周期类型--月'''
    _purchaseTimesTypeChosen_month=("xpath",'//li[text()="月"]')

    '''计划信息-添加   elements'''
    _planinfoAdd=("css selector","button.layui-btn.layui-btn-normal.layui-btn-sm")
    '''名称'''
    _name = ("css selector","[name='name']")
    '''规格型号'''
    _model = ("css selector","[name='specification']")
    '''数量'''
    _num = ("css selector","[name='num']")
    '''单价'''
    _price = ("css selector","[name='price']")
    '''品牌'''
    _brand =("css selector","[name='brand']")
    '''上传'''
    _upload =("css selector",".layui-upload-file")
    '''提交'''
    _submit = ("css selector","#submit")

    '''与我相关'''
    _related_button = ("xpath","//a[text()='与我相关']")

    '''审核'''
    _check = ("xpath","//button[text()='审核']")

    '''同意'''
    _agree=("xpath","//button[text()='同意']")

    '''打回'''
    _disagree=("css selector","#disagree")

    '''第一条待审核计划'''
    _first_plan = ("css selector","#exampleTable > tbody > tr:nth-child(1) > td:nth-child(3) > a")

    '''计划单号输入框 elements'''
    _planID_input = ("css selector","#pid")

    '''查询 elements'''
    _select=("css selector"," button.btn.btn-success")

    '''第一条审批状态 '''
    _check_status=("css selector",".badge_diy")

    '''删除'''
    _delete = ("css selector",".btn.btn-danger.btn-sm")

    '''删除--确定'''
    _accept=("css selector",".layui-layer-btn0")



    def check_first_agree(self):

        self.into_plan_detail()
        self.into_check_detail()
        self.agree_plan()

    def check_first_disagree(self):
        self.into_plan_detail()
        self.into_check_detail()
        self.disagree_plan()

    '''进入与我相关'''
    def into_related_to_myself(self):
        self.click_element(self._related_button)
        frames = self.driver.find_elements_by_tag_name("iframe")
        self.switch_iframe(frames[1])


    '''进入计划详情'''
    def into_plan_detail(self):
        # frames = self.driver.find_elements_by_tag_name("iframe")
        # self.switch_iframe(frames[1])

        self.get_elements(self._first_plan,0).click()

    def into_check_detail(self):
        frames = self.driver.find_elements_by_tag_name("iframe")
        self.switch_iframe(frames[0])
        sleep(1)
        self.click_element(self._check)
        # driver.find_element_by_xpath("//button[text()='审核']").click()

    def agree_plan(self):
        frames = self.driver.find_elements_by_tag_name("iframe")
        self.switch_iframe(frames[0])
        sleep(1)
        # driver.find_element_by_xpath("//button[text()='同意']").click()
        self.click_element(self._agree)

    def disagree_plan(self):
        frames = self.driver.find_elements_by_tag_name("iframe")
        self.switch_iframe(frames[0])
        sleep(1)
        self.click_element(self._disagree)


    def into_add(self):
        frames2 = self.driver.find_elements_by_tag_name("iframe")
        self.switch_iframe(frames2[0])

        self.click_element(self._add)
        frames = self.driver.find_elements_by_tag_name("iframe")
        self.switch_iframe(frames[0])




    def add_plan(self,title,purchaseTimes,name,model,num,price,brand):
        self.input_text(self._title,title)
        self.click_element(self._type)
        self.click_element(self._type_mechina_buy)
        self.input_text(self._purchaseTimes,purchaseTimes)
        self.click_element(self._purchaseTimesTypeChosen)
        self.click_element(self._purchaseTimesTypeChosen_month)
        self.click_element(self._planinfoAdd)
        self.input_text(self._name,name)
        self.input_text(self._model,model)
        self.input_text(self._num,num)
        self.input_text(self._price,price)
        self.input_text(self._brand,brand)
        # self.upload_file(self._upload,file)

        self.click_element(self._submit)
        sleep(1)

    '''获取新增的采购计划编号'''
    def get_planID(self):
        self.back_defaultFrame()
        sleep(1)
        frames1 = self.driver.find_elements_by_tag_name("iframe")
        self.switch_iframe(frames1[1])
        self.into_related_to_myself()
        sleep(1)
        select_ele = self.get_elements(self._select,0)
        select_ele.click()
        ele = self.get_elements(self._first_plan,0)
        return ele.get_attribute("text")


    '''获取全部审批同意的状态'''
    def select_plan_status(self,planID):
        '''iframe0'''
        # frames1 = self.driver.find_elements_by_tag_name("iframe")
        # self.switch_iframe(frames1[1])
        '''tab_iframe'''
        frames2 = self.driver.find_elements_by_tag_name("iframe")
        self.switch_iframe(frames2[0])
        # for child_frame in self.driver.find_elements_by_tag_name("iframe"):
        #     child_frame_id = child_frame.get_attribute("name")
        #     print("当前frame是{}".format(child_frame_id))

        planID_ele = self.get_elements(self._planID_input,0)
        planID_ele.send_keys(planID)
        select_ele = self.get_elements(self._select,0)
        select_ele.click()

        sleep(1)
        # status = self.driver.find_element_by_css_selector(".badge_diy").text
        # return status
        return self.get_check_status()


    def get_check_status(self):
        ele = self.get_element(self._check_status)
        return ele.text


    '''获取打回的审批状态'''
    def get_disagree_check_status(self):
        self.back_defaultFrame()
        sleep(1)
        frames1 = self.driver.find_elements_by_tag_name("iframe")
        self.switch_iframe(frames1[1])
        self.into_related_to_myself()
        sleep(1)
        select_ele = self.get_elements(self._select,0)
        select_ele.click()
        status=self.get_check_status()
        return status

    def delete_end_plan(self):
        sleep(1)
        self.click_element(self._delete)
        self.click_element(self._accept)