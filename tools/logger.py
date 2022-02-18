# -*- coding: UTF-8 -*-
import os
import logging
from config.config import LOG_PATH
from tools.times import datetime_strftime


class Log:

    def __init__(self):
        self.logger = logging.getLogger()
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)

            # 创建一个handle写入文件
            fh = logging.FileHandler(self.log_path, encoding='utf-8')
            fh.setLevel(logging.INFO)

            # 创建一个handle输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            # 定义输出的格式
            formatter = logging.Formatter(self.fmt)
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # 添加到handle
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    @property
    def log_path(self):
        if not os.path.exists(LOG_PATH):
            os.makedirs(LOG_PATH)
        return os.path.join(LOG_PATH, '{}.log'.format(datetime_strftime()))

    @property
    def fmt(self):
        return '%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s'


log = Log().logger


if __name__ == '__main__':
    log.info('')
