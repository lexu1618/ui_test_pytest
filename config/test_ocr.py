from common.handler_ini import Handle_ini

data = Handle_ini("setting.ini").get_all_section()
print(data)

# data1 =Handle_ini("setting.ini").get_all_options("sqlserver")
# print(data1)
# print(type(data1))


# dict = dict(data1)
# print(dict)
# db_config = {'host': '172.16.19.243',
#                      'port': '1433',
#                      'database': 'aerator',
#                      'user': 'sa',
#                      'password': 'sae',
#                      'as_dict': True}

# dict1 = {"a": "   true"}
# if isinstance(dict1["a"], str):
#     dict1["a"] = (dict1["a"]).strip().lower() in "true"
#     print(dict1["a"])
#
# for k,v in data1.items():
#     if isinstance(v,str):
#         if v.strip().lower() in "true" :
#          data1[k] =True
#         elif v.strip().lower() in "false" :
#          data1[k] = False
# print(data1)

from config.path import *
import pymysql

db_config = Handle_ini(setting_path).get_all_options("mysql")
print(db_config)
comn = pymysql.connect(**db_config)




