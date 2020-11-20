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


    def into_add(self):
        self.click_element(self._add)
        frames = self.driver.find_elements_by_tag_name("iframe")
        self.switch_iframe(frames[0])


    def add_plan(self,title,purchaseTimes,name,model,num,price,brand,file):
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
        self.upload_file(self._upload,file)
        sleep(1)
        self.click_element(self._submit)

