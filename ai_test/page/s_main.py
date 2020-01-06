'''
@Time    : 2019/12/26 11:45
@Author  : fzj
@Desc    : 学生端主页面
'''
from poium import Page, PageElement
from page.s_xiaole import Xiaolepage

class Mainpage(Page):
    xiaole_loc = PageElement(class_name='enterxiaole')
    wood_loc = PageElement(class_name='wood')

    def task(self):
        #首页任务
        pass

    def hi_xiaole(self):
        #小乐同学
        self.xiaole_loc.click()
        return Xiaolepage(self.driver)

    def wood(self):
        #学习森林
        self._wood_loc.click()

