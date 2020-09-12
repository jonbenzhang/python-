from django.db import models


class UserGroup(models.Model):
    """
    部门
    """
    title = models.CharField(max_length=32)


"""
# 增加
models.UserGroup.objects.create(title='销售部')
# 删除
models.UserGroup.objects.filter(id=2).delete()
# 修改
models.UserGroup.objects.filter(id=2).update(title='公关部')
# 查看
group_list = models.UserGroup.objects.all()
group_list = models.UserGroup.objects.filter(id=1)
# id__gt=1，为大于1,__gt为大于
# id__lt=1，为小于1,__lt为小于
group_list = models.UserGroup.objects.filter(id__gt=1)
group_list = models.UserGroup.objects.filter(id__lt=1)
"""


class UserInfo(models.Model):
    """
    员工
    """
    nid = models.BigAutoField(primary_key=True)
    user = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=1)
    # ug_id
    ug = models.ForeignKey("UserGroup", null=True, on_delete=models.CASCADE)
