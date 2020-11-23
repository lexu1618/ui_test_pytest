from Common.handle_yaml import HandleYaml

data = HandleYaml.read_alone("scenario_data.yaml")["test_add_first_disagree"]
print(data)

d = {'add': {'username': 'shh4', 'password': '111111', 'title': '采购计划102', 'purchaseTimes': '1', 'name': '设备1',
             'model': '大型', 'num': 1, 'price': 50, 'brand': 'zxc', 'check1': {'username': 'shh3', 'password': '111111'},
             'check2': {'username': 'shh2', 'password': '111111'}}}

d2 = {'add': {'username': 'shh4', 'password': '111111', 'title': '采购计划102', 'purchaseTimes': '1', 'name': '设备1',
              'model': '大型', 'num': 1, 'price': 50, 'brand': 'zxc'},
      'check1': {'username': 'shh3', 'password': '111111'}, 'check2': {'username': 'shh2', 'password': '111111'}}
