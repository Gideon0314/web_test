# -*- coding: UTF-8 -*-
import os
import configparser
from config.config import INI_PATH

HOST = 'HOST'


class ReadConfig:
    """配置文件"""

    def __init__(self):
        if not os.path.exists(INI_PATH):
            raise FileNotFoundError("配置文件%s不存在！" % INI_PATH)
        self.config = configparser.RawConfigParser()  # 当有%的符号时请使用Raw读取
        self.config.read(INI_PATH, encoding='utf-8')

    def __get(self, section, option):
        """获取"""
        return self.config.get(section, option)

    def __set(self, section, option, value):
        """更新"""
        self.config.set(section, option, value)
        with open(INI_PATH, 'w') as f:
            self.config.write(f)

    @property
    def url(self):
        return self.__get(HOST, HOST)


ini = ReadConfig()

if __name__ == '__main__':
    print(ini.url)
