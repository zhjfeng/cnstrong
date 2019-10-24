import uiautomator2 as u2
import time
import pytest

d = u2.connect()

#pyperclip.copy('￥FZLcYqqFEs2￥')
d.app_start('com.tencent.mm')
d(resourceId="com.tencent.mm:id/k_").click()
#d.xpath("//android.widget.ImageView").click()
d(resourceId="com.tencent.mm:id/m6").click()
d.send_keys("￥FZLcYqqFEs2￥")
#d.long_click("//android.widget.EditText[@text='￥FZLcYqqFEs2￥']", 0.5)
d(resourceId="com.tencent.mm:id/m6").long_click(0.5)
d(text="全选").click()
d(text="复制").click()

d.app_start('com.taobao.taobao')
d(text="打开").click()





'''
import pytest

import pytest
@pytest.mark.parametrize("test_input,expected",
                         [ ("3+5", 8),
                           ("2+4", 6),
                           ("6 * 9", 42),
                         ])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

@pytest.fixture()
#@pytest.fixture(scope="session")
def open():
    print("setup——打开浏览器，打开百度首页")

    yield
    print("teardown——关闭浏览器")

def test_case1(open):
    print("搜索python")

def test_case2(open): 
    print("搜索pytest")

def test_case3(open):
    print("搜索uiautomator")


@pytest.fixture()
def login():
    print("登录")

def test_1(login):
    print("我的需登录")

def test_2():  # 不传login
    print("首页")

def test_3(login):
    print("个人中心需登录")
'''
