from flask import request
import os
import xlrd
# 获取到名为file的文件，也可以使用for循环递归读取
file = request.files["file"]
# 文件保存
file.save(os.path.join(".", "113.txt"))
# 文件名称
filename = file.filename
#读取文件内容
file_read = file.read()
# read和save不能同时使用，save后file.read()会读取到空的内容
#使用excel直接读取，
wb = xlrd.open_workbook(file_contents=file_read)