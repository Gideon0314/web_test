# -*- coding: UTF-8 -*-
import pytest
from page_action.components import Components
from page_action.welcome import Welcome
from page_action.ai import AiDashboard


class TestAi:

    @pytest.mark.usefixtures("login_by_token")
    # @pytest.mark.usefixtures("login_by_mobile")
    def test_001(self, drivers):
        """进入AI智能营销"""
        welcome = Welcome(drivers)
        ai = welcome.enter_ai()
        ai.menu_check()

    def test_002(self, drivers):
        system = Components(drivers)
        system.change_system_case()

    def test_003(self, drivers):
        """AI智能营销-数据看板"""
        ai = AiDashboard(drivers)
        ai.manage_check()
        # ai.details_check()


if __name__ == '__main__':
    pytest.main(['-s', 'TestCase/test_002_ai.py'])
