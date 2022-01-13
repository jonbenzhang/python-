# myproxy.py
from functools import partial
from tag1_0_1.werkzeug.local import LocalProxy


class Boss(object):
    def pop(self):
        print('Ok')
        return 'OK'


# class OtherObj(object):
#     def __init__(self, Obj):
#         self.real_obj = Obj()


# other = OtherObj(Boss)


def get_boss(Obj=None):
    return Boss()


proxy_boss = LocalProxy(get_boss)
proxy_boss.pop()