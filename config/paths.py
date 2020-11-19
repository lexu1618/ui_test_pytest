from pathlib import Path


'''配置文件目录路径'''
CONFIG_PATH = Path(__file__).resolve().parents[0]
'''测试数据目录路径'''
DATA_PATH = Path(__file__).resolve().parents[1]/'data'
'''测试日志目录路径'''
LOGS_PATH = Path(__file__).resolve().parents[1]/'logs'
'''测试报告目录路径'''
REPORTS_PATH = Path(__file__).resolve().parents[1]/'reports'
'''测试用例目录路径'''
TESTS_PATH = Path(__file__).resolve().parents[1]/'tests'
"""WEB异常截图"""
SCREENSHOOTS_PATH = Path(__file__).resolve().parents[1]/'logs'/'screenshoots'


''' 1、获取当前文件绝对路径 '''
# current_path = Path(__file__).resolve()

''' 2、获取当前文件上 n 级目录 '''
# current_path.parents[n-1]
# Path(__file__).resolve().parents[n-1]

''' 3、路径拼接 '''
# demo_path = current_path.parents[1]/'conf'/'demo.txt'
# with open(demo_path, 'x', encoding='UTF-8') as f:
#     f.write('hello world')

''' 4、判断一个路径表示的文件或文件夹是否真的存在 '''
# Path.exists(path)

''' 5、创建目录 '''
# if not Path.exists(directory_path):
#     Path.mkdir(directory_path)

''' 6、判断一个路径表示的是否是一个文件 '''
# Path.is_file(path)

''' 7、判断一个路径表示的是否是一个文件夹 '''
# Path.is_dir(path)

''' 8、获取当前工作目录 '''
# print(Path.cwd())
