from email.mime.text import MIMEText
from email.utils import formataddr
import smtplib
# Content-Type: text/plain; charset="utf-8"
# MIME-Version: 1.0
# Content-Transfer-Encoding: 7bit
# Subject: title
# From: jenbonzhang@126.com
# To: 15732132531@163.com
# Date: Tue, 19 Jan 2021 21:28:47 +0800
# Message-ID: <161106292753.28000.5380203109731225606@zhangmengcomputer>

def mail():
    msg = MIMEText('张先生今天吃得啥', 'plain', 'utf-8')
    msg["Subject"] = "title"
    msg['From'] = formataddr(["zhangling", 'jenbonzhang@126.com'])
    msg['To'] = formataddr(["zhangmeng",'15732132531@163.com'])
    print(msg.as_string())
    server = smtplib.SMTP()
    server.connect("smtp.126.com")
    try:
        server.login("jenbonzhang@126.com", "YWYGLQNOPLWNNJJY")
    except:
        print("login failed")
    server.sendmail('jenbonzhang@126.com', ["1901329664@qq.com",'15732132531@163.com',"jenbonzhang@gmail.com"], msg.as_string())
    server.quit()


if __name__ == '__main__':
    mail()
