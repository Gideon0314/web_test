# -*- coding: UTF-8 -*-
import requests


def get_token(name, pw):
    url = "http://test.api.sso.skytech.cn/login"
    data = {
        'name': name,
        'password': pw,
        'token': True,
    }
    headers = {
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'Content-Type': "application/json",
        'Accept-Encoding': 'gzip, deflate, br',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }
    response = requests.request("POST", url, json=data, headers=headers)
    if response.status_code == 200 and response.json()['desc'] == "success":
        user_token = response.json()['token']
        return user_token
    return print(response.status_code)
