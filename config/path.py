
import os


root_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]


setting_path = os.path.join(root_path,"config","setting.ini")

log_path = os.path.join(root_path,"Outputs","logs")

report_path = os.path.join(root_path,"Outputs","reports")

screenShot_path = os.path.join(root_path,"Outputs","screenshots")

chromeDrive_path = os.path.join(root_path,"chromedriver.exe")

print(screenShot_path +"\page.png")

# test_login_data_path  = os.path.join(root_path,"test_data","login_data.yaml")
#
# test_register_data_path  = os.path.join(root_path,"test_data","register_data.yaml")
#
# test_loginlog_data_path = os.path.join(root_path,"test_data","loginlog_data.yaml")
#
# test_operlog_data_path = os.path.join(root_path,"test_data","operlog_data.yaml")
#
# base_data_path = os.path.join(root_path,"test_data","base_data.yaml")
#
# dev_data_path = os.path.join(root_path,"test_data","device_data.yaml")
#
# sensor_data_path = os.path.join(root_path,"test_data","sensor_data.yaml")

if __name__ == '__main__':
    print(root_path)
    print(setting_path)