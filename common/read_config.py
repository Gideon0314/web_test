# -*- coding: UTF-8 -*-
import os
from config.config import YAML_PATH
import yaml


class ReadConfig:
    """配置文件"""

    def __init__(self):
        if not os.path.exists(YAML_PATH):
            print(YAML_PATH)
            raise FileNotFoundError("yaml配置文件不存在")
        with open(YAML_PATH, 'r') as yamlfile:
            self.cfg = yaml.safe_load(yamlfile)

    @property
    def get_cfg(self):
        """获取"""
        return self.cfg


cfg = ReadConfig().get_cfg


if __name__ == '__main__':
    pass
