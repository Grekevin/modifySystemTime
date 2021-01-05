# -*- conding:utf-8 -*-

import json
import os

class Config(object):
    def __init__(self):
        super().__init__()
        self.config_file_name = 'config.ini'
        self.config_file_path = None
        self.create_config_file()

    # 配置文件是否存在，不存在，则创建   
    def create_config_file(self):
        self.config_file_path = os.path.join(os.path.dirname(__file__), self.config_file_name)
        exist_flag = os.path.exists(self.config_file_path)
        if not exist_flag:
            with open(self.config_file_path, 'w', encoding='utf-8') as f:
                f.write('')
            print('配置文件已创建！')

    # 写入数据
    def write_data(self, name, url):
        read_data = self.read_data()
        with open(self.config_file_path, 'w', encoding='utf-8') as f:
            if not read_data:
                read_data = {}
            read_data[name] = url
            data = json.dumps(read_data, ensure_ascii=False)
            f.write(data)
            print('成功写入数据！')


    # 读取数据
    def read_data(self):
        with open(self.config_file_path, 'r', encoding='utf-8') as f:
            read_data = f.read()
            if not read_data:
                return {}
            print('读取数据成功！')
            return json.loads(read_data)


def main():
    cfg = Config()
    cfg.create_config_file()
    cfg.read_data()


if __name__ == "__main__":
    main()