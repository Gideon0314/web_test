# -*- coding: UTF-8 -*-
from page.base_page import BasePage, sleep
from common.read_element import Element


components = Element('components')


class Components(BasePage):
    """通用组件-多页面使用"""

    def cust_name(self):
        return self.element_text(components['客户名称'])

    def package_name(self):
        return self.element_text(components['套餐'])

    def user_role(self):
        self.is_click(components['登录用户名称'])
        print(self.element_text(components['用户角色']))
        return self.element_text(components['用户角色'])

    def click_web(self):
        self.is_click(components['网站'])

    def check_web_icon(self):
        self.is_click(components['跳转网站图标'])
        sleep(5)
        self.close_page()

    def change_system(self, sys):
        self.is_click(components['切换系统'])
        self.is_click(components[sys])

    def change_system_case(self):
        self.change_system('CRM客户管理系统')
        self.change_system('外贸智能云建站')
        self.change_system('SNS跨平台云社交系统')
        self.change_system('Google广告管理系统')
        self.change_system('Facebook广告管理系统')
        self.change_system('智能营销')
