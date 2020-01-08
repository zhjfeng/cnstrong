'''
@Time    : 2019/12/26 11:06
@Author  : fzj
@Desc    : 浏览器驱动
'''

from selenium import webdriver
from page.login import Loginpage
class Web:

    @classmethod
    def s_start(cls):
        #学生按分辨率启动
        WIDTH = 960
        HEIGHT = 600
        PIXEL_RATIO = 3.0
        UA = 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'

        mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO},
                           "userAgent": UA}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        cls.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        return Loginpage(cls.driver)

    @classmethod
    def p_start(cls):
        #家长按手机模式启动
        mobileEmulation = {'deviceName': 'iPhone X'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        cls.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        cls.driver.implicitly_wait(10)
        return Loginpage(cls.driver)

    @classmethod
    def quit(cls):
        cls.driver.quit()