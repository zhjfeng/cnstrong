import uiautomator2 as u2
import time

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
    d(description=u"捉猫猫").click()
    '''
    d(text="打开").click()
    time.sleep(3)
    
    i = 1
    while True:
        
    #拆红包
        j = "J_MM_RED_COVER_" + str(i) + "_0"
        print(j)
        if d(resourceId=j).exists:
            d(resourceId=j).click()
    #再拆一次
            d.xpath("//android.view.View[@text='再拆一次']").click()
            continue
        i += 1
        
        if i >=4:
            break

    #进入活动
    d(text="TB1SC2xj8v0gK0jSZKbXXbK2FXa-322-76.png_360x10000.jpg_").click()
     '''
    #做任务领猫币
    d(text="gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==", className="android.widget.Image", instance=13).click()
    
    while True:
        time.sleep(3)
        if d(text="去浏览").exists:
            d(text="去浏览").click()
            print('去浏览会场')
            time.sleep(25)
            d(description="转到上一层级").click()
            continue
        elif d(text="去进店").exists:
            d(text="去进店").click()
            print('去浏览店铺')
            time.sleep(25)
            d(description="转到上一层级").click()
            continue
        else:
            print("结束了")
            break

def jd_11():
    d.app_start('com.jingdong.app.mall')
    d(description=u"浮层icon").click()
#wx_copy()

tb_11()

