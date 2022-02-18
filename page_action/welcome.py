# -*- coding: UTF-8 -*-
from page.base_page import BasePage, sleep
from common.read_element import Element
from page_action.ai import AiDashboard

welcome = Element('welcome')
components = Element('components')


class Welcome(BasePage):
    """欢迎页"""

    def popup_close(self):
        sleep(2)
        self.is_click(welcome['新功能弹窗关闭'])

    def enter_ai(self):
        self.is_click(welcome['AI大数据'])
        return AiDashboard(self.driver)


if __name__ == '__main__':
    pass
