# @Author：LOUIE
# @Time：2020/3/10 19:25

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.read_config import rc
from email.header import Header
from smtplib import SMTP
from common.config_log import log
import os
import time


"""
1.定义邮箱头部
2.定义邮箱正文
3.定义邮箱附件
4.获取最新的报告，读取报告
5.写入附件
6.发送邮件
"""


class ConfigEmail():

    def __init__(self):
        self.username = rc.get_email("username")
        self.password = rc.get_email("password")
        self.host = rc.get_email("host")
        self.port = rc.get_email("port")
        self.sender = rc.get_email("sender")
        self.content = rc.get_email("content")
        self.on_off = rc.get_email("on_off")
        self.subject = rc.get_email("subject")
        self.value = rc.get_email("recievers")
        self.recievers = []
        if "/" in str(self.value):
            self.recievers.append(str(self.value).split("/"))
        else:
            self.recievers = self.value
        self.msg = MIMEMultipart()
        self.smtp = SMTP()

    def email_header(self):
        """
        定义邮件头部信息
        :return:
        """
        self.msg["From"] = self.sender
        self.msg["To"] = self.recievers
        self.msg["Subject"] = self.subject

    def email_content(self):
        """
        定义邮件正文
        :return:
        """
        content = MIMEText(self.content, _subtype="plain", _charset="utf-8")
        self.msg.attach(content)

    def check_file(self):
        """
        排序后读取最新的报告文件
        :return:
        """
        REPORT_PATH = os.path.join(rc.PROJECT_PATH, "report")
        if not os.path.exists(REPORT_PATH):
            os.mkdir(REPORT_PATH)
        listdir = os.listdir(REPORT_PATH)
        if len(listdir) == 0:
            log.info("报告存放路径为空，请检查文件夹")
            return FileNotFoundError
        else:
            listdir.sort(key=lambda x: os.path.getmtime(REPORT_PATH + "\\" + x))
            att_file = os.path.join(REPORT_PATH, listdir[-1])
        return att_file

    def email_attchment(self):
        att_file = self.check_file()
        with open(att_file, mode="w+", encoding="utf8") as file:
            attachment = MIMEText(file)
        date = time.strftime("%Y-%m-%d")
        att_name = date + "# TestReport.html"
        attachment["Content-Disposition"] = 'attachment; filename={}'.format(att_name)
        self.msg.attach(att_name)

    def send_email(self):
        """
        发送邮件步骤：
        1.连接域名和端口号
        2.登录邮箱
        3.传入邮箱文本内容
        4.发送邮件
        5.关闭smtp连接
        :return:
        """
        self.email_header()
        self.email_content()
        self.check_file()
        self.email_attchment()
        try:
            self.smtp.connect(self.host, self.port)
        except:
            return ConnectionError
        try:
            # 注意username 应该一致，否则会报错
            self.smtp.login(self.username, self.password)
            self.smtp.sendmail(self.username, self.password, self.msg.as_string())
        except TimeoutError:
            log.error("////// 发送邮件超时，请检查连接")
        except Exception as e:
            log.error("////// 发送邮件失败，错误：%e" %e)
        finally:
            self.smtp.close()
            self.smtp.quit()


ce = ConfigEmail()


if __name__ == '__main__':
    pass
