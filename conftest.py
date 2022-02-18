# -*- coding: UTF-8 -*-
import os
import base64
import pytest
import allure
from py._xmlgen import html
from selenium import webdriver
from common.read_config import cfg
from config.config import SCREENSHOT_DIR
from tools.send_email import send_report
from tools.times import datetime_strftime, timestamp
from common.inspect import inspect_element
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = None
curpath = os.path.dirname(os.path.realpath(__file__))
chrome = os.path.join(curpath, 'drivers/chromedriver.exe')
data = r'C:\Users\Gideon\AppData\Local\Google\Chrome\User Data\Default'


@pytest.fixture(scope='session', autouse=True)
def drivers(request):
    global driver
    if driver is None:
        chrome_options = Options()
        chrome_options.add_argument(f'--user-data-dir={data}')
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('disable-gpu')
        # chrome_options.add_argument('blink-settings=imagesEnabled=false')
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver = webdriver.Chrome(service=Service(chrome), options=chrome_options)
        driver.maximize_window()
    def fn():
        driver.quit()
    request.addfinalizer(fn)
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            screen_img = _capture_screenshot()
            if screen_img:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:1024px;height:768px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('用例名称'))
    cells.insert(2, html.th('Test_nodeid'))
    cells.pop(2)


def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.nodeid))
    cells.pop(2)


def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
        data.append(html.div('通过的用例未捕获日志输出.', class_='empty log'))


def pytest_html_report_title(report):
    report.title = "pytest测试报告"


def pytest_configure(config):
    config._metadata.clear()
    config._metadata['测试项目'] = "测试项目"
    config._metadata['测试地址'] = cfg['HOST']


def pytest_html_results_summary(prefix, summary, postfix):
    # prefix.clear() # 清空summary中的内容
    prefix.extend([html.p("所属部门: 技术部")])
    prefix.extend([html.p("测试执行人: Gideon")])


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """收集测试结果"""
    result = {
        "total": terminalreporter._numcollected,
        'passed': len(terminalreporter.stats.get('passed', [])),
        'failed': len(terminalreporter.stats.get('failed', [])),
        'error': len(terminalreporter.stats.get('error', [])),
        'skipped': len(terminalreporter.stats.get('skipped', [])),
        # terminalreporter._sessionstarttime 会话开始时间
        'total times': timestamp() - terminalreporter._sessionstarttime
    }
    print(result)
    if result['failed'] or result['error']:
        send_report()


def _capture_screenshot():
    """截图保存为base64"""
    now_time, screen_file = timestamp(), SCREENSHOT_DIR
    driver.save_screenshot(screen_file)
    allure.attach.file(screen_file,
                       "失败截图{}".format(now_time),
                       allure.attachment_type.PNG)
    with open(screen_file, 'rb') as f:
        imagebase64 = base64.b64encode(f.read())
    return imagebase64.decode()
