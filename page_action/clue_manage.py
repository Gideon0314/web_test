# -*- coding: UTF-8 -*-
# -*- coding: UTF-8 -*-
from page.base_page import BasePage
from common.read_element import Element
from tools.times import sleep

clue_manage = Element('crm/clue_manage')


class ClueManage(BasePage):
    """搜索类"""

    def search_check(self):
        """查询"""
        sleep(10)
        self.input_text_slow(clue_manage['名称或邮箱地址'], 'tjd0314@126.com')
        sleep(100)
