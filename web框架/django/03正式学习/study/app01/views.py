from django.shortcuts import render, HttpResponse
from app01 import models
from django.views import View


class Login(View):
    """
    get     查
    post    创建
    put     更新
    delete  删除
    """

    def dispatch(self, request, *args, **kwargs):
        print('before')
        obj = super(Login, self).dispatch(request, *args, **kwargs)
        print('after')
        return obj

    def get(self, request):
        # return HttpResponse('Login.get')
        return render(request, 'login.html')

    def post(self, request):
        print(request.POST.get('user'))
        return HttpResponse('Login.post')


def b():
    a = models.UserGroup.objects.first()
    print(a)
    return HttpResponse("test")


from django.core.paginator import Paginator, Page, PageNotAnInteger, EmptyPage


def index(request):
    """
    分页
    :param request:
    :return:
    """
    # for i in range(300):
    #     name = "root" + str(i)
    #     models.UserInfo.objects.create(name=name,age=18,ut_id=1)

    current_page = request.GET.get('page')

    user_list = models.UserInfo.objects.all()
    paginator = Paginator(user_list, 10)
    # per_page: 每页显示条目数量
    # count:    数据总个数
    # num_pages:总页数
    # page_range:总页数的索引范围，如: (1,10),(1,200)
    # page:     page对象
    try:
        posts = paginator.page(current_page)
    except PageNotAnInteger as e:
        posts = paginator.page(1)
    except EmptyPage as e:
        posts = paginator.page(1)
    # has_next              是否有下一页
    # next_page_number      下一页页码
    # has_previous          是否有上一页
    # previous_page_number  上一页页码
    # object_list           分页之后的数据列表
    # number                当前页
    # paginator             paginator对象
    return render(request, 'index.html', {'posts': posts})
