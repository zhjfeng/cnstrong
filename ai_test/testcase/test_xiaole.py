'''
@Time    : 2019/12/26 17:26
@Author  : fzj
@Desc    : 小乐demo
'''

from page.login import Loginpage
import pytest

class TestXaiole():

    def test_xiaole(self,browser):
        self.xiaole_page = Loginpage(browser).login('955112', 'a1234567').hi_xiaole()
        self.xiaole_page.question('三角函数')
        assert '123' in self.xiaole_page.get_answer()

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_xiaole.py"])
