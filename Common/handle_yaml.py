import yaml
import logging
class HandleYaml:
    # 读取yaml文件
    @staticmethod
    def read_alone(yaml_file):
        if yaml_file == None:
            logging.info("文件名为空")
        else:
            try:
                with open(yaml_file,encoding="UTF-8") as f:
                    data = yaml.load(f,Loader=yaml.FullLoader)
                return data
            except Exception as e:
                logging.info("文件名错误")
                raise e

    # 读取yaml文件,返回一个可迭代对象，要配合循环使用
    @staticmethod
    def read_all(yaml_file):
        if yaml_file == None:
            logging.info("文件名为空")
        else:
            try:
                with open(yaml_file,encoding="UTF-8") as f:
                    data = yaml.load_all(f,Loader=yaml.FullLoader)
                return data
            except Exception as e:
                logging.info("文件名错误")
                raise e
    @staticmethod
    def write_alone(yaml_file, context):
        if yaml_file == None:
            logging.info("文件名为空")
        else:
            try:
                with open(yaml_file, 'w', encoding='utf8') as f:
                    return yaml.dump(context, f)
            except Exception as e:
                logging.info("文件名错误")
                raise e

    @staticmethod
    def write_all(yaml_file, context):
        if yaml_file == None:
            logging.info("文件名为空")
        else:
            try:
                with open(yaml_file, 'w', encoding='utf8') as f:
                    return yaml.dump_all(list(context), f)
            except Exception as e:
                logging.info("文件名错误")
                raise e

if __name__ == '__main__':
    pass