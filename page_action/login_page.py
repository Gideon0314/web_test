# -*- coding: UTF-8 -*-
from page.base_page import BasePage, sleep
from common.read_element import Element
from page_action.welcome import Welcome


login = Element('login')


class LoginPage(BasePage):
    """搜索类"""

    def click_toggle(self, phone, code):
        """输入"""
        self.is_click(login['切换验证码登录'])
        self.input_text(login['手机号'], phone)
        self.input_text(login['验证码'], code)

    def click_login(self):
        """点击登录"""
        self.is_click(login['登录'])
        return Welcome(self.driver)

    def code_hint(self):
        pass


if __name__ == '__main__':
    pass
