# EPXUEQJXIMLHIEJL
# EPXUEQJXIMLHIEJL
from flask_old import Flask
from flask_mail import Mail
from flask_mail import Message

app = Flask(__name__)
# MAIL_SERVER	邮件服务器地址，默认为 localhost
# MAIL_PORT	邮件服务器端口，默认为 25
# MAIL_USE_TLS	是否启用传输层安全 (Transport Layer Security, TLS)协议，默认为 False
# MAIL_USE_SSL	是否启用安全套接层 (Secure Sockets Layer, SSL)协议，默认为 False
# MAIL_DEBUG	是否开启 DEBUG，默认为 app.debug
# MAIL_USERNAME	邮件服务器用户名，默认为 None
# MAIL_PASSWORD	邮件服务器密码，默认为 None
# MAIL_DEFAULT_SENDER	邮件发件人，默认为 None，也可在 Message 对象里指定
# MAIL_MAX_EMAILS	邮件批量发送个数上限，默认为 None
# MAIL_SUPPRESS_SEND	默认为 app.testing，如果为 True，则不会真的发送邮件，供测试用
app.config['MAIL_SERVER'] = 'smtp.126.com'
# port=25 【不使用TLS】
# 或
# port=465 【使用TLS】
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "jenbonzhang@126.com"
# app.config['MAIL_PASSWORD'] = "1234509876zmzl!"
app.config['MAIL_PASSWORD'] = "YWYGLQNOPLWNNJJY"
# app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
# app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <youremail@163.com>'


mail = Mail(app)


# def send_async_email(app, msg):
#     with app.app_context():
#         mail.send(msg)
#
# def send_email(to, subject, template, **kwargs):
#     msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
#     msg.body = render_template(template + '.txt', **kwargs)
#     msg.html = render_template(template + '.html', **kwargs)
#     thr = Thread(target=send_async_email, args=[app, msg])
#     thr.start()
#     return thr

@app.route("/", methods=["GET"])
def send_emain_simple():
    text = """
    这里是body,判断一下作用
    无用
    无用
    """
    html = """
    <h4>你好啊</h4>
    <h3>你好啊</h3>
    <a href="www.baidu.com">这里是百度</a>
    """
    # html 和body同时使用
    # html中的内容会把body中的内容覆盖掉
    message = Message(sender="jenbonzhang@126.com", subject='title', recipients=['15732132531@163.com'], body=text,
                      html=html)
    print(message)
    mail.send(message)
    return {}


if __name__ == '__main__':
    app.run(port=8888)
    # send_emain_simple()
