'''
Project:页面基本操作方法：如click_next_btn
'''
from selenium.webdriver.common.by import By
from page.base_page import BasePage

# 继承BasePage类
class GuidPage(BasePage):
    # 元素
    _next_btn_loc = (By.NAME, 'loginName')

    # 点击下一步
    def click_login(self):
        self.find_element(*self._next_btn_loc).click()