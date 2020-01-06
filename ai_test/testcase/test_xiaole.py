'''
@Time    : 2019/12/26 17:26
@Author  : fzj
@Desc    : 小乐demo
'''

from poium import Page, PageElement
import sys
sys.path.append("E:\\git\\cnstrong\\ai_test")
from page.web import Web
from page.main import Mainpage

class TestXaiole():
    def setup(self):
        self.xiaole_page = Web.s_start().login('955112', 'a1234567').hi_xiaole()

    def test_xiaole(self):
        self.xiaole_page.question()

    def teardown(self):
        pass