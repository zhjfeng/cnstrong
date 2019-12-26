# -*- coding: utf-8 -*-
'''
心理测评pad端H5页面答题脚本
author：zhjfeng
date：20190111

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re
import random

class EduplanImport(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        time.sleep(3)
        self.driver.implicitly_wait(30)
        self.base_url = "https://cas.leke.cn/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_eduplanceping(self):        
        driver = self.driver
        driver.get(self.base_url + "login")
        time.sleep(2)
        driver.find_element_by_id("loginName").clear()
        driver.find_element_by_id("loginName").send_keys("xxxxx")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("xxxxxx")
        driver.find_element_by_id("j-sign-on").click()
        #driver.find_element_by_link_text(u"升学规划").click()
        driver.get("https://eduplan.leke.cn/auth/hd/epassessment/myEpassessmentStart.htm?typeId=1")
        time.sleep(2)
        #开始第一部分
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/input").click()        
        #第一部分测评
        for x in range(2,62):
            #随机选项
            y = (random.randint(2,3))
            driver.find_element_by_xpath("/html/body/div[1]/div/div[" + str(x) + "]/div/div[2]/p[" + str(y) + "]/i").click()
            time.sleep(1)
        #完成第一部分    
        driver.find_element_by_xpath("/html/body/div[1]/div/div[62]/div/div[2]/div/input").click()  
        #进入第二部分
        driver.find_element_by_xpath("/html/body/div[1]/div/div[63]/div/div/input").click()        
        #第二部分测评
        for x in range(64,124):
            y = (random.randint(2,3))
            driver.find_element_by_xpath("/html/body/div[1]/div/div[" + str(x) + "]/div/div[2]/p[" + str(y) + "]/i").click()
            time.sleep(1)
        #继续
        driver.find_element_by_xpath("/html/body/div[1]/div/div[124]/div/div[2]/div/input").click()
        #开始第三部分
        driver.find_element_by_xpath("/html/body/div[1]/div/div[125]/div/div/input").click()
        #第三部分测评
        for x in range(126,226):
            y = (random.randint(2,5))
            driver.find_element_by_xpath("/html/body/div[1]/div/div[" + str(x) + "]/div/div[2]/p[" + str(y) + "]/i").click()
            time.sleep(1)
        #提交评测，注释了，需要手动提交
        #driver.find_element_by_xpath("//*[@id="comit"]").click()       
        
if __name__ == "__main__":
    unittest.main()
'''
from selenium import webdriver
import random
import time

mobile = {'deviceName': 'iPhone X'}
path = 'C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobile)
driver = webdriver.Chrome(path, chrome_options=options)
driver.get('https://cas.leke.cn/login?service=')
driver.find_element_by_name('loginName').send_keys('955194')
driver.find_element_by_name('password').send_keys('jia1234567@')
driver.find_element_by_id('jLogin').click()
driver.get('http://webapp.leke.cn/leke-ai-h5/#/redirect?enter=1')
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[3]/a/span').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div/div/div[3]/a/span').click()
time.sleep(3)
for x in range(0, 20):
    y = (random.randint(1, 5))
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/div[" + str(y) + "]/div[1]").click()
    time.sleep(2)



