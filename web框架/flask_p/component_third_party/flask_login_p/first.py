import flask_ as flask

app = flask.Flask(__name__)
# 这是加密密钥
app.secret_key = 'super secret string'  # Change this!

import flask_login
# from source_code import flask_login

login_manager = flask_login.LoginManager()

login_manager.init_app(app)
# 当作是一个数据库,存储用户信息
users = {'aaa': {'password': 'bbb'}}


class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']

    return user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''

    email = flask.request.form['email']
    if flask.request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        # 注册该用户登陆
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))

    return 'Bad login'


@app.route('/protected')
# 登陆验证，如果没有登陆不能访问
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id


# 退出登陆
@app.route('/logout')
@flask_login.login_required
def logout():
    # 退出当前用户
    flask_login.logout_user()
    return flask.redirect(flask.url_for('login'))


@app.route("/cookie")
def cookie():
    from flask_old import request
    print(request.cookies.get("login_key"))
    return {}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003)
