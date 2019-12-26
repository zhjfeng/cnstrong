# -*- encoding=utf8 -*-
__author__ = "fengzj"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.android.android import Android
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/4ef6899d",
    ])

# script content
print("start...")
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
devs = device()
#print(devs.list_app(third_only=True))

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
'''
#京东签到领券
start_app('com.jingdong.app.mall',activity=None)
sleep(2.0)
poco(text="领券").click()
poco("com.jd.lib.coupon:id/a_8").click()
sleep(2.0)
stop_app('com.jingdong.app.mall')
'''
#start_app('com.eg.android.AlipayGphone',activity=None)
#poco(text="蚂蚁森林").click()
'''
#偷取能量
def get_power():
    list_power = poco("J_barrier_free").children()
#print(list_node)
    for power in list_power:
        name = power.get_name()
        #print(name)
        #print(node.get_name())    
        if  name.find("收集能量") >= 0:
            power.click()
    poco("com.alipay.mobile.nebula:id/h5_tv_nav_back").click()

while exists(Template(r"tpl1559121271633.png", record_pos=(0.477, 0.574), resolution=(1080, 2280))) != False:
    touch(Template(r"tpl1559121515597.png", record_pos=(0.478, -0.46), resolution=(1080, 2280)))
    poco("com.alipay.mobile.nebula:id/h5_tv_nav_back").click()
'''

swipe([],[])


