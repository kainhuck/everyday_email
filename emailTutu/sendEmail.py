import os
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from config import email

sender = email["sender"]
password = email["password"]
mailHost = email["mailHost"]
receivers = email["receivers"]

def sendEmail(subject, msgContent, attachment=None):
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = sender
    msgContent = msgContent
    msg.attach(MIMEText(msgContent, 'html', 'utf-8'))

    # 附件: 目前支持一张图片
    if attachment:
        try:
            filename = os.path.basename(attachment)
            with open(attachment, 'rb') as f:
                # 设置附件的MIME和文件名，这里是jpg类型,可以换png或其他类型:
                mime = MIMEBase('image', 'jpg', filename=filename)
                # 加上必要的头信息:
                mime.add_header('Content-Disposition', 'attachment', filename=filename)
                mime.add_header('Content-ID', '<0>')
                mime.add_header('X-Attachment-Id', '0')
                # 把附件的内容读进来:
                mime.set_payload(f.read())
                # 用Base64编码:
                encoders.encode_base64(mime)
                # 添加到MIMEMultipart:
                msg.attach(mime)
        except Exception as e:
            print("附件发送失败", e)

    # 登录并发送邮件
    try:
        # QQsmtp服务器的端口号为465或587
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.set_debuglevel(1)
        s.login(sender, password)
        for item in receivers:
            msg['To'] = to = item
            s.sendmail(sender, to, msg.as_string())
            print('Success!')
        s.quit()
        print("All emails have been sent over!")
    except smtplib.SMTPException as e:
        print("Falied,%s", e)
