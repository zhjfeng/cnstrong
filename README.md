
plublic下是公共业务模块（已集成到jenkins）；

YAPI_test 是配合集成在jenkins定时执行的接口自动化脚本，用来判断每次测试是否通过，当有用例测试失败时发送邮件到项目组提醒的脚本（已集成到jenkins，任务名：YAPI）；

eduplan 是用在升学规划业务下的一些脚本
xinliceping是用来随机在客户端点击选项，完成心理测评测试的脚本；
addcache是用来批量添加平行志愿的脚本；

elk_test 是抓取ELK平台上，项目组当天报错日志的脚本，如有报错，截取报错数量和信息发送给项目组成员（已集成到jenkins，任务名：ELK_test）；

del_swagger 是删除swagger中，移动端和pad端的接口的脚本（已集成到jenkins，任务名：swagger）；

webcrawler下主要是一些爬虫脚本：

swyt 是抓取浙江教育考试院高考信息中和三位一体相关内容的脚本，如出现新的三位一体咨询，发送邮件给项目组成员（已集成到jenkins，任务名：sanweiyiti）；

gkzy_zsurl 是抓取高考志愿网中的招生官网地址的脚本；

college_zsurl 是爬取院校官网中和招生相关的链接的脚本；

collegezsurl_test 是检测招生和院校官网的死链接的脚本；
