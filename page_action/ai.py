# -*- coding: UTF-8 -*-
from page.base_page import BasePage
from common.read_element import Element

ai = Element('ai/ai')


class AiDashboard(BasePage):
    """AI营销"""

    def menu_check(self):
        self.is_click(ai['天擎天拓服务'])
        self.is_click(ai['网站访客识别'])
        self.is_click(ai['网站访客自动营销'])
        self.is_click(ai['发件箱'])
        self.is_click(ai['草稿箱'])
        self.is_click(ai['角色权限'])
        self.is_click(ai['子账户管理'])
        self.is_click(ai['客户设置'])
        self.is_click(ai['系统设置'])
        self.is_click(ai['营销设置'])
        self.is_click(ai['数据看板'])

    # def details_check(self):
    #     self.is_click(ai['最近网站访问-查看详情'])
    #     self.back()
    #     self.is_click(ai['广告恶意点击防御-查看详情'])
    #     self.back()
    #     self.is_click(ai['最近邮件询盘-查看详情'])
    #     self.back()
    #     self.is_click(ai['最近messenger询盘-查看详情'])
    #     self.back()
    #     self.is_click(ai['最近表单询盘-查看详情'])


    def manage_check(self):
        self.scroll_bar(ai['线索看板-查看详情'])
        self.back()
        self.scroll_bar(ai['Google Ads广告报告-查看详情'])
        self.back()
        self.scroll_bar(ai['Facebook Ads广告报告-查看详情'])
        self.back()

    def topsky_service(self):
        self.is_click(ai['天擎天拓服务悬浮框'])
        self.is_click(ai['天擎天拓服务悬浮-服务详情'])
        self.back()

    def clue_check(self):
        self.is_click(ai['最近表单询盘-查看详情'])
        return


if __name__ == '__main__':
    pass
