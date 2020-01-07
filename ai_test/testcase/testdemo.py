'''
@Time    : 2019/12/23 16:58
@Author  : fzj
@Desc    : 用例demo
'''

from page.web import Web

class TestDemo:
    def setup(self):
        self.login_page = Web.s_start()

    def test_login(self):
        self.login_page.login('955112', 'a1234567')

    def teardown(self):
        pass
