# -*- coding: UTF-8 -*-
import os
from config.config import YML_PATH
import yaml


class ReadConfig:
    """配置文件"""

    def __init__(self):
        if not os.path.exists(YML_PATH):
            raise FileNotFoundError("配置文件%s不存在！" % 'C:\Test_Helper\web_test\config\config.yml')
        with open(YML_PATH, 'r') as ymlfile:
            self.cfg = yaml.safe_load(ymlfile)

    @property
    def get_cfg(self):
        """获取"""
        return self.cfg


cfg = ReadConfig().get_cfg


if __name__ == '__main__':
    pass
