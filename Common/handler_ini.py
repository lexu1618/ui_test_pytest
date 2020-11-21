import configparser
from configparser import NoSectionError,NoOptionError
import logging

'''
如果 ini文件中有特殊字符
使用 RawConfigParser()方法进行读取即可，代码如下：

1 config=configparser.RawConfigParser()
'''
class Handle_ini:
    def __init__(self,ini_file):
            self.cf = configparser.ConfigParser()
            data = self.cf.read(ini_file)
            # cf.read方法返回的是一个列表，如果为空，则说明路径错误或者ini文件为空
            if data ==[]:
                logging.info("ini文件不存在或ini文件内容为空")
                raise FileNotFoundError

#   获取所有section的值
    def get_all_section(self):
        try:
            sections = self.cf.sections()
            return sections
        except NoSectionError as e:
            logging.ino("NoSectionError: section is not exists")
            raise e



    #获取指定section下option的值，返回一个字典形式
    def get_all_options(self,section):
        try:
            value = self.cf.items(section)     #这里的items 是configparser模块中的方法，参数是section，返回的是一个列表嵌套元祖，
            data = dict(value)                    #通过dict()方法 可以把元祖转换成字典
            for k, v in data.items():         # 这里是处理读取ini文件后，布尔值变成字符串，所以要转换成布尔值
                if isinstance(v, str):
                    if v.strip().lower() in "true":
                        data[k] = True
                    elif v.strip().lower() in "false":
                        data[k] = False
                if k == "port":            #对端口号进行强转，必须是整型
                    data[k] = int(v)
            return data
        except Exception as e:
            logging.info("NoSectionError: 没有指定的{}".format(section))
            raise e

    #获取指定section，option 的值
    """
        #     获取指定section和option对应的数据
        #     如果option对应数据为数字，则自动转换为int或者float
        #     如果option对应的数据是个可以使用eval转换的类型，则传递flag为True时，自动转换,否则输出str
        #     
    """
    def get_option_value(self,section,option,flag=False):
        try:
            value = self.cf[section][option]     #这里的items 是configparser模块中的方法，参数是section，返回的是一个列表
            if value.isdigit():
                return int(value)
            try:
                return float(value)
            except Exception :
                pass
            if isinstance(flag,bool) and flag:
                return eval(value)
            else:
                return value
        except (NoSectionError,NoOptionError) as e:
            logging.info("NoSectionError: 没有指定的{}{}".format(section,option))
            raise e



if __name__ == '__main__':
        from config.path import setting_path
        hand_ini = Handle_ini(setting_path)
        data = hand_ini.get_option_value("host","api_root_url")
        print(data)
        print(type(data))
