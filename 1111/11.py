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
def tb_mb():
    d.app_start('com.taobao.taobao')
    d(description=u"捉猫猫").click()
    '''
    d(text="打开").click()
    time.sleep(3)
    while True:    
    #拆红包
        if d(text="恭喜发财，大吉大利").exists:
            d(text="恭喜发财，大吉大利").click()
            print('拆红包')
    #再拆一次
            d.xpath("//android.view.View[@text='再拆一次']").click()
            time.sleep(3)
            continue
        else:
            print('没有红包机会了')
            break

    #进入活动
    d(text="TB1SC2xj8v0gK0jSZKbXXbK2FXa-322-76.png_360x10000.jpg_").click()
    while True:
        if d(text="开心收下").exists:
            d(text="开心收下").click()
        else:
            break
'''
    #做任务领猫币
    d(text=u"领喵币").click()
    if d(text="签到").exists:
        d(text="签到").click()
    while True:
        time.sleep(3)
        if d(text="去浏览").exists:
            d(text="去浏览").click()
            print('去浏览会场')
            time.sleep(25)
            d(description="转到上一层级").click()
            continue
        if d(text="去进店").exists:
            d(text="去进店").click()
            print('去浏览店铺')
            time.sleep(25)
            d(description="转到上一层级").click()
            continue
        else:
            print("结束了")
            break

def jd_wc():
    time.sleep(3)
    #返回，因为店铺和会场按钮元素不一致，所以用相对坐标
    d.click(0.068, 0.066)
    d(text=u"朕知道了").click(timeout=5)

def jd_11():
    d.app_start('com.jingdong.app.mall')
    d(description=u"浮层icon").click()
    time.sleep(5)
    #点击领金币因为元素抓取不到，用了相对坐标
    #print(d(className="android.view.View", instance=57))
    d.click(0.892, 0.773)
    
    i = 0
    while True:        
        if d(text=u"逛逛好店（"+str(i)+"/25个）").exists:
            d(text=u"逛逛好店（"+str(i)+"/25个）").click()
            print('去逛逛好店'+str(i))
            jd_wc()

        if d(text=u"精选好物（"+str(i)+"/25个）").exists:
            d(text=u"精选好物（"+str(i)+"/25个）").click()
            print('去精选好物'+str(i))
            jd_wc()

        if i>=25:
            print('结束了')
            break  
        print(i)   
        i +=1
        
#jd_11()
def jd_1():
    d.app_start('com.jingdong.app.mall')
    d(description=u"浮层icon").click()
    time.sleep(5)
    #点击领金币因为元素抓取不到，用了相对坐标
    #print(d(className="android.view.View", instance=57))
    d.click(0.892, 0.773)
    

       
    
    d(text="精选好物（5/25个）").click()
    print('去精选好物')
    jd_wc()
tb_mb()
'''
#互动
d(className="android.view.View", instance=38)
d(className="android.view.View", instance=38)
'''