'''
@Time    : 2019/12/26 11:45
@Author  : fzj
@Desc    : 学生端主页面
'''
from poium import Page, PageElement

class Main(Page):
    _xiaole_loc = PageElement(class_name='enterxiaole')
    _wood_loc = PageElement(class_name='wood')

    def task(self):
        #首页任务
        self.get("http://webapp.leke.cn/leke-ai-pad/#/operation")
        return self

    def xiaole(self):
        #小乐同学
        self._xiaole_loc.click()
        return self

    def wood(self):
        #学习森林
        self._wood_loc.click()

