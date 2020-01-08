'''
@Time    : 2019/12/23 16:58
@Author  : fzj
@Desc    : 用例demo
'''

import pytest
from page.login import Loginpage

class TestDemo:

    def test_login(self,browser):
        self.login_page = Loginpage(browser)
        self.login_page.login('955112', 'a1234567')


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_demo.py"])