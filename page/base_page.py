# -*- coding: UTF-8 -*-
# from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from config.config import LOCATE_MODE
from tools.times import sleep
from tools.logger import log
# from selenium.webdriver.common.keys import Keys


class BasePage:
    """selenium基类"""

    time = 20

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_url(self, url):
        """打开网址并验证"""
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(30)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            log.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时请检查网络或网址服务器" % url)

    @staticmethod
    def element_locator(func, locator):
        """元素定位器"""
        name, value = locator
        return func(LOCATE_MODE[name], value)

    def find_element(self, locator, timeout=time):
        """寻找单个元素"""
        self.wait = WebDriverWait(self.driver, timeout)
        return BasePage.element_locator(lambda *args: self.wait.until(
            ec.presence_of_element_located(args)), locator)

    def find_elements(self, locator, timeout=time):
        """查找多个相同的元素"""
        self.wait = WebDriverWait(self.driver, timeout)
        return BasePage.element_locator(lambda *args: self.wait.until(
            ec.presence_of_all_elements_located(args)), locator)

    def elements_num(self, locator):
        """获取相同元素的个数"""
        number = len(self.find_elements(locator))
        log.info("相同元素：{}".format((locator, number)))
        return number

    def input_text(self, locator, txt):
        """输入(输入前先清空)"""
        sleep(1)
        ele = self.find_element(locator)
        ele.clear()
        ele.send_keys(txt)
        log.info("输入文本：{}".format(txt))

    def input_text_slow(self, locator, txt):
        """输入(输入前先清空)"""
        sleep(1)
        ele = self.find_element(locator)
        ele.clear()
        for i in list(txt):
            ele.send_keys(i)
            sleep(1)
        log.info("输入文本：{}".format(txt))

    def is_click(self, locator, timeout=time):
        """点击"""
        self.find_element(locator, timeout).click()
        sleep(1)
        log.info("点击元素：{}".format(locator))

    def element_text(self, locator):
        """获取当前的text"""
        _text = self.find_element(locator).text
        log.info("获取文本：{}".format(_text))
        return _text

    @property
    def get_source(self):
        """获取页面源代码"""
        return self.driver.page_source

    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
        self.driver.implicitly_wait(30)

    def back(self):
        """后退"""
        self.driver.back()
        self.driver.implicitly_wait(30)

    def now_page(self):
        now_page = self.driver.current_window_handle
        self.driver.switch_to.window(now_page)

    def close_page(self):
        now_page = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != now_page:
                self.driver.switch_to.window(handle)
                self.driver.close()
        self.driver.switch_to.window(now_page)

    def check_element(self, locator):
        try:
            self.find_element(locator)
            return True
        except Exception as e:
            log.error(e)
            return False

    def scroll_bar(self, locator):
        js = "return document.body.scrollHeight"
        # 获取滚动条的高度
        new_height = self.driver.execute_script(js)
        for i in range(0, new_height, 100):
            try:
                self.is_click(locator, timeout=3)
                return True
            except Exception as e:
                log.info('未找到该元素，继续滑动', e)
                self.driver.execute_script('window.scrollTo(0, %s)' % i)
                continue
