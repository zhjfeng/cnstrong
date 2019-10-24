import uiautomator2 as u2
import time
import pytest

d = u2.connect()
#打开微信复制淘口令
def wx_copy():
    d.app_start('com.tencent.mm')
    d(resourceId="com.tencent.mm:id/k_").click()
    d(resourceId="com.tencent.mm:id/m6").click()
    d.send_keys("￥FZLcYqqFEs2￥")
    d(resourceId="com.tencent.mm:id/m6").long_click(0.5)
    d(text="全选").click()
    d(text="复制").click()

#领双11红包并刷猫币
def tb_11():
    d.app_start('com.taobao.taobao')
    #d(text="打开").click()
    d(description=u"捉猫猫").click()
    #d(text="TB1SC2xj8v0gK0jSZKbXXbK2FXa-322-76.png_360x10000.jpg_").click()
    d(text="gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==", className="android.widget.Image", instance=13).click()
    
    while d(text="去浏览").exists:
        d(text="去浏览").click()
        time.sleep(20)
        d(description="转到上一层级").click()
    else:
        while d(text="去进店").exists:
            d(text="去进店").click()
            time.sleep(20)
            d(description="转到上一层级").click()


def jd_11():
    pass

tb_11()
