'''
@Time    : 2019/12/26 17:26
@Author  : fzj
@Desc    : 小乐demo
'''

from page.web import Web

class TestXaiole():
    def setup(self):
        self.xiaole_page = Web.s_start().login('955112', 'a1234567').hi_xiaole()

    def test_xiaole(self):
        self.xiaole_page.question('三角函数')
        self.xiaole_page.answer_loc()

    def teardown(self):
        pass