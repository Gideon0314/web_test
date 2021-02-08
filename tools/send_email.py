# -*- coding: UTF-8 -*-
import os
import smtplib
import yagmail
from config.config import EMAIL_INFO, ADDRESSEE


def send_email(recipient, headline, contents):
    yag = yagmail.SMTP(**EMAIL_INFO)
    # 发送邮件
    return yag.send(recipient, headline, contents)


def send_report(report=None):
    # 报告目录
    """发送报告"""
    # with open(REPORT_PATH, encoding='UTF-8') as f:
    #     html = f.read()
    recipient = ADDRESSEE
    headline = '测试报告'
    contents = [
        '附件为本次测试结果',
        report
    ]

    try:
        send_email(recipient, headline, contents)
        print('定时邮件询盘发送成功，请验收')
    except smtplib.SMTPException as e:
        print(f"Error: 无法发送邮件,{e}")


if __name__ == "__main__":
    '''请先在config/config.py文件设置邮箱的账号和密码'''
    pass
    # send_report()
