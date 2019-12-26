'''
@Time    : 2019/12/21 16:03
@Author  : fzj
@Desc    : 登录页
'''
from poium import Page, PageElement

class Loginpage(Page):
    _loginname_loc = PageElement(name='loginName')
    _password_loc = PageElement(name='password')
    _login_loc = PageElement(id_='jLogin')

    def login(self,loginname,password):
        self.get("https://cas.leke.cn/login?service=")
        self._loginname_loc = loginname
        self._password_loc = password
        self._login_loc.click()
        return self