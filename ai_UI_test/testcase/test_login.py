import unittest
from page.login_page import LoginPage
from selenium import webdriver
from page.web import Web

class Caselogin(unittest.TestCase):

    def setUp(self):
        self.login_page = Web.start().LoginPage()
        '''
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.url = "https://cas.leke.cn/login?service="
        self.loginName = "955112"
        self.password = "a1234567"
        '''
    # 用例执行体
    def test_login(self):
        self.login_page.input_loginName('955112')
        self.login_page.input_password('a1234567')
        self.login_page.click_login()
        '''
        # 声明LoginPage类对象
        login_page = LoginPage(self.driver, self.url, "乐课网 - 我们的快乐课堂")
        # 调用打开页面组件
        login_page.open()
        
        # 切换到登录框Frame
        #login_page.switch_frame('x-URS-iframe')
        # 调用用户名输入组件
        login_page.input_loginName(self.loginName)
        # 调用密码输入组件
        login_page.input_password(self.password)
        # 调用点击登录按钮组件
        login_page.click_login()
        '''
    def tearDown(self):
        pass
        #self.driver.quit()


if __name__ == "__main__":
    unittest.main()