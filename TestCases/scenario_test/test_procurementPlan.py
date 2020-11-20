

class TestProcuremnetPlan:


    def test_add(self,login):
        index_page = login
        buy_plan_page = index_page.into_buyPlan()
        buy_plan_page.into_add()
        buy_plan_page.add_plan("1","1","1","1","1","1","1",r"D:\requirements.txt")