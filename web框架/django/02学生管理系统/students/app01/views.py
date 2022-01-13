from django.shortcuts import render, redirect, HttpResponse
import pymysql
import json


def classes(request):
    if not request.get_signed_cookie("cookie_key", salt="qazwsx"):
        return redirect("/login/")
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='zhang', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id,title from class")
    class_list = cursor.fetchall()
    cursor.close()
    conn.close()

    return render(request, 'classes.html', {'class_list': class_list})


def add_class(request):
    if request.method == "GET":
        return render(request, 'add_class.html')
    else:
        print(request.POST)
        v = request.POST.get('title')
        if len(v) > 0:
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='zhang',
                                   charset='utf8')
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            cursor.execute("insert into class(title) values(%s)", [v, ])
            conn.commit()
            cursor.close()
            conn.close()
            return redirect('/classes/')
        else:
            return render(request, 'add_class.html', {'msg': '班级名称不能为空'})


def del_class(request):
    nid = request.GET.get('nid')

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='zhang', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("delete from class where id=%s", [nid, ])
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/classes/')


def edit_class(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='zhang', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id,title from class where id = %s", [nid, ])
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        print(result)
        return render(request, 'edit_class.html', {'result': result})
    else:
        nid = request.GET.get('nid')
        title = request.POST.get('title')

        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='zhang', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("update class set title=%s where id = %s", [title, nid, ])
        conn.commit()
        cursor.close()
        conn.close()

        return redirect('/classes/')


def students(request):
    """
    学生列表
    :param request: 封装请求相关的所有信息
    :return:
    """
    #
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='zhang', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(
        "select student.id,student.name,class.title from student left JOIN class on student.class_id = class.id")
    student_list = cursor.fetchall()
    cursor.execute("select id,title from class")
    class_list = cursor.fetchall()
    cursor.close()
    conn.close()

    return render(request, 'students.html', {'student_list': student_list, 'class_list': class_list})


def add_student(request):
    if request.method == "GET":
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='zhang', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id,title from class")
        class_list = cursor.fetchall()
        cursor.close()
        conn.close()

        return render(request, 'add_student.html', {'class_list': class_list})
    else:
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='zhang', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("insert into student(name,class_id) values(%s,%s)", [name, class_id, ])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/students/')


from utils import sqlheper


def edit_student(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        class_list = sqlheper.get_list("select id,title from class", [])
        current_student_info = sqlheper.get_one('select id,name,class_id from student where id=%s', [nid, ])
        return render(request, 'edit_student.html',
                      {'class_list': class_list, 'current_student_info': current_student_info})
    else:
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        sqlheper.modify('update student set name=%s,class_id=%s where id=%s', [name, class_id, nid, ])
        return redirect('/students/')


# ############################ 对话框 ############################


def modal_add_class(request):
    title = request.POST.get('title')
    if len(title) > 0:
        sqlheper.modify('insert into class(title) values(%s)', [title, ])
        return HttpResponse('ok')
    else:
        return HttpResponse('班级标题不能为空')


def modal_edit_class(request):
    data = {"code": 200, "message": ""}
    try:
        id = request.POST.get('id')
        title = request.POST.get('title')
        if len(title) > 0 and len(id) > 0:
            sqlheper.modify('update  class set title=%s where id=%s', [title, id])
    except Exception as e:
        data['code'] = 400
        data["message"] = "异常"
    ret = json.dumps(data)
    return HttpResponse(ret)


def model_add_student(request):
    data = {"code": 200, "message": ""}
    try:
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        if len(class_id) > 0 and len(name) > 0:
            sqlheper.modify('insert into student(name, class_id) values(%s,%s)', [name, class_id])
    except Exception as e:
        print(e)
        data['code'] = 400
        data["message"] = "异常"
    ret = json.dumps(data)
    return HttpResponse(ret)


def model_edit_student(request):
    data = {"code": 200, "message": ""}
    try:
        id = request.POST.get('id')
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        if len(id) > 0:
            sqlheper.modify('update  student set name=%s,class_id=%s where id=%s', [name, class_id, id])
    except Exception as e:
        data['code'] = 400
        data["message"] = "异常"
    ret = json.dumps(data)
    return HttpResponse(ret)


# 多对多，以老师表展示
def teachers(request):
    # teacher_list = sqlheper.get_list('select id,name from teacher',[])
    teacher_list = sqlheper.get_list("""
      select teacher.id as tid,teacher.name,class.title from teacher
        LEFT JOIN teacher2class on teacher.id = teacher2class.teacher_id
        left JOIN class on class.id = teacher2class.class_id;
    """, [])
    print(teacher_list)
    result = {}
    for row in teacher_list:
        tid = row['tid']
        if tid in result:
            result[tid]['titles'].append(row['title'])
        else:
            result[tid] = {'tid': row['tid'], 'name': row['name'], 'titles': [row['title'], ]}

    return render(request, 'teacher.html', {'teacher_list': result.values()})


def add_teacher(request):
    if request.method == "GET":
        class_list = sqlheper.get_list("select * from class", [])
        return render(request, "add_teacher.html", class_list)
    else:
        name = request.POST.get("name")
        class_ids = request.POST.get("class_ids")
        # 插入一个老师,获取到他的id
        teacher_id = sqlheper.create("insert into teacher(name,) values %s", [name, ])
        # 插入班级和老师的对应
        # 多次连接多次提交
        # for class_id in class_ids:
        #     sqlheper.modify("insert into teacher2class(teacher_id, class_id) values %s, %s", [teacher_id, class_id])
        # 一次连接提交所有
        data_lists = [[teacher_id, class_id] for class_id in class_ids]
        con = sqlheper.SqlHelper()
        con.multiple_modify("insert into teacher2class(teacher_id, class_id) values %s, %s", data_lists)
        con.close()
        return redirect("/teachers/")


def edit_teacher(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        obj = sqlheper.SqlHelper()
        teacher_info = obj.get_one('select id,name from teacher where id =%s', [nid, ])
        class_id_list = obj.get_list('select class_id from teacher2class where teacher_id=%s', [nid, ])
        class_list = obj.get_list('select id,title from class', [])
        obj.close()

        print('当前老师信息', teacher_info)
        print('当前老师任教的班级id', class_id_list)
        temp = []
        for i in class_id_list:
            temp.append(i['class_id'])
        print('所有班级', class_list)
        # return HttpResponse('...')
        return render(request, 'edit_teacher.html', {
            'teacher_info': teacher_info,
            'class_id_list': temp,
            'class_list': class_list,
        })
    else:
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        class_ids = request.POST.getlist('class_ids')
        obj = sqlheper.SqlHelper()
        # 更新老师表
        obj.modify('update teacher set name=%s where id=%s', [name, nid])
        # 更新老师和班级关系表
        # 先把当前老师和班级的对应关系删除，然后再添加
        obj.modify('delete from teacher2class where teacher_id=%s', [nid, ])

        data_list = []
        for cls_id in class_ids:
            temp = (nid, cls_id,)
            data_list.append(temp)
        # map?lambda表达式？
        obj = sqlheper.SqlHelper()
        obj.multiple_modify('insert into teacher2class(teacher_id,class_id) values(%s,%s)', data_list)
        obj.close()

        return redirect('/teachers/')


def get_all_class(request):
    obj = sqlheper.SqlHelper()
    class_list = obj.get_list('select id,title from class', [])
    obj.close()
    return HttpResponse(json.dumps(class_list))


def modal_add_teacher(request):
    ret = {'status': True, 'message': None}
    try:
        name = request.POST.get('name')
        class_id_list = request.POST.getlist('class_id_list')

        teacher_id = sqlheper.create('insert into teacher(name) values(%s)', [name, ])

        data_list = []
        for cls_id in class_id_list:
            temp = (teacher_id, cls_id,)
            data_list.append(temp)
        obj = sqlheper.SqlHelper()
        obj.multiple_modify('insert into teacher2class(teacher_id,class_id) values(%s,%s)', data_list)
        obj.close()
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)
    return HttpResponse(json.dumps(ret))


def layout(request):
    return render(request, "layout.html")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        if user == 'z' and pwd == '123':
            return_data = redirect("/classes/")
            import datetime
            from datetime import timedelta
            ct = datetime.datetime.utcnow()
            v = timedelta(seconds=10)
            value = ct + v
            # cookie_key cookie的key值
            # cookie_value cookie的value值
            # expires设置cookie的超时时间
            # max_age　也是设置cookie的超时时间单位秒
            # salt 对cookie进行加密,默认只是后面添加了时间戳，可以通过配置进行自定义加密方式
            return_data.set_cookie()
            return_data.set_signed_cookie("cookie_key", "cookie_value", expires=value, salt="qazwsx")
            return return_data
        else:
            return redirect("/login/")
