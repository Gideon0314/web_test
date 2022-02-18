# -*- coding: UTF-8 -*-
import pytest
from common.read_config import cfg
from page_action.login_page import LoginPage
from page_action.welcome import Welcome
from tools.get_token import get_token


@pytest.fixture(scope='session')
def login_by_mobile(drivers):
    """登录"""
    phone = '16602140314'
    code = '123'
    login = LoginPage(drivers)
    login.get_url(cfg['HOST'])
    login.click_toggle(phone, code)
    login.click_login()
    welcome = Welcome(drivers)
    welcome.popup_close()

@pytest.fixture(scope='session')
def login_by_token(drivers):
    login = LoginPage(drivers)
    # mobile = ''
    # pw = ''
    # token = get_token(mobile, pw)
    token = 'e38022e9ae77485aae898ed287f2b1da'
    login.get_url(f'https://my.iglobalwin.com/?token={token}')
    # token = 'ae7e39987e8c4c2ab5c1e245108a6fe3'
    # login.get_url(f'https://test.my.iglobalwin.com/?token={token}')
    # login.get_url(f'{host}/?token={token}')
    welcome = Welcome(drivers)
    welcome.popup_close()
