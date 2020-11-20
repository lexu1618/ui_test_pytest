import os


base_dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

testdatas_dir = os.path.join(base_dir,"TestDatas")

testcases_dir = os.path.join(base_dir,"TestCases")

report_dir = os.path.join(base_dir,"Outputs/reports")

log_path = os.path.join(base_dir,"Outputs/logs")

setting_path = os.path.join(base_dir,"config","setting.ini")



screenshot_path = os.path.join(base_dir,"Outputs","screenshots")


login_data_dir = os.path.join(base_dir,"TestDatas","login_data.yaml")

personData_data_dir = os.path.join(base_dir,"TestDatas","personData_data.yaml")



index_data_dir = os.path.join(base_dir,"TestDatas","index_data.yaml")


common_data_dir = os.path.join(base_dir,"TestDatas","common_data.yaml")



scenario_data_dir = os.path.join(base_dir,"TestDatas","scenario_data.yaml")