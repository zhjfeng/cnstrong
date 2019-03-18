#coding:utf-8
'''
邮件组件
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

def send_email(receiver,title,body):
    mail_host="smtp.cnstrong.cn"  #设smtp置服务器
    mail_user="X@cnstrong.cn"    #登录邮箱
    mail_pass="XXXXXXXX"   #授权码
    sender = 'XXXXXX@cnstrong.cn'#发送邮箱

    message = MIMEText(body , 'plain', 'utf-8')
    
    message['From'] = Header("升学规划测试组", 'utf-8')
    message['To'] =  Header("升学规划项目组", 'utf-8')
 
    subject = title
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(sender, receiver, message.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("无法发送邮件")

if __name__ == '__main__':
    send_email()