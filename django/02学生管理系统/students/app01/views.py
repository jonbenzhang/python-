from django.shortcuts import render, redirect, HttpResponse
import pymysql
import json


def classes(request):
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
