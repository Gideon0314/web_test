# -*- coding: UTF-8 -*-
import pytest
from time import sleep
from tools.logger import log
from common.read_config import cfg
from page_action.components import Components
from page_action.login_page import LoginPage
from page_action.welcome import Welcome


class TestLogin:

    @pytest.mark.usefixtures("login_by_token")
    # @pytest.mark.usefixtures("login_by_mobile")
    def test_001(self, drivers):
        """访问网站"""
        # welcome = Welcome(drivers)
        # welcome.popup_close()
        components = Components(drivers)
        components.check_web_icon()
        sleep(3)

    @pytest.mark.parametrize("role", ["管理员"])
    def test_002(self, role, drivers):
        """用户角色校验"""
        components = Components(drivers)
        user_role = components.user_role()
        assert user_role == role


if __name__ == '__main__':
    pytest.main(['-s', 'TestCase/test_001_login.py'])
