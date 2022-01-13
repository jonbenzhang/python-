# django
## 创建一个django项目
first 是要创建的项目的名称
```shell script
django-admin startproject first
```
## 目录结构

![image-20200902170152905](/home/zhangmeng/.config/Typora/typora-user-images/image-20200902170152905.png)

1.  init__.py:是项目的初始化文件有了这个文件 标志当前文件夹是一个包,可以被引用

2. settings.py:项目的配置文件，所有的django的配置信息都在这里面,包括数据库的配置,静态文件的配置,还有django依赖的第三方扩展包

3. urls.py：进行url路由的配置，通过网址对应网页

4. wsgi.py：服务器和django交互的入口

5. manage.py:是项目的管理文件

   ## 配置文件修改

   在配置文件中有详细的修改说明

   1. 配置模板路径
   2. 配置静态文件路径