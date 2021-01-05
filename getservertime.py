# -*- coding:utf-8 -*-

import time
import requests
import json


class ServerTime(object):
    def __init__(self, config_data, server_name):
        super().__init__()
        self.config_data = config_data
        self.server_name = server_name

    # 获取服务器时间
    def get_datetime(self):
        HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
            }
        server_data = json.loads(requests.get(self.config_data[self.server_name], headers=HEADERS).text)
        
        if self.server_name in ['淘宝服务器', '天猫服务器']:
            return self.parse_time(float(server_data['data']['t'])/1000)
        elif self.server_name == '京东服务器':
            return self.parse_time(float(server_data['serverTime'])/1000)
        elif self.server_name == '苏宁服务器':
            return server_data['sysTime2']

    # 把服务器时间解析成字符串返回
    def parse_time(self, server_time):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(server_time))

def main():
    name = '天猫服务器'
    url = 'http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp'
    data = {name:url}
    server_time = ServerTime(data, name)
    print(server_time.get_datetime())

if __name__ == "__main__":
    main()