from selenium.webdriver.remote.webdriver import WebDriver
from page.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from page.base_page import BasePage

class Web(BasePage):
    driver:WebDriver=None
    def start(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

        self.login_page = self._open("https://cas.leke.cn/login?service=", "乐课网 - 我们的快乐课堂")
        return LoginPage(self.driver)

    def quit(self):
        self.driver.quit()

'''
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.url = "https://cas.leke.cn/login?service="
        cls.loginName = "955112"
        self.password = "a1234567"
'''

