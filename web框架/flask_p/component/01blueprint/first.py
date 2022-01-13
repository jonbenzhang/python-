from source_code.flask import Blueprint, render_template, abort, url_for
from jinja2 import TemplateNotFound

# 定义一个蓝图
# simple_page是蓝图名
simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')


@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)


from source_code.flask import Flask

app = Flask(__name__)
app.register_blueprint(simple_page)
# 蓝图可定义挂载位置
# 这样就会在/pages/下寻找对应的url
app.register_blueprint(simple_page, url_prefix='/pages')
print(app.url_map)
print(simple_page.root_path)
"""
# url_for 跳转向蓝图的内的端点，把蓝图名作为前缀
url_for('simple_page.index')
# url_for 跳转向当前蓝图的内的端点，把前面加一个点
url_for('.index')
"""
