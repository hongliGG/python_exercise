# 通过__new__ 实现单例模式
'''
__init__ 是初始化一个类实例
__new__ 是创建一个类的实例
实现思想： 
1. 先给_instance 复制一个空
2. 判断这个类的_instance 是否空， 如果是创建一个新实例给_instance，并返回
'''
class Single(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Single, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pass


single1 = Single()
single2 = Single()

print(id(single1) == id(single2))


# 装饰器实现
'''
1. function 需要明确产参数
2. method 不需要传参数
类直接调用是function，类的实例调用的是method 
'''
def single(cls):
    def inner():
        if not hasattr(cls, '_instance'):
            cls._instance = cls
        return cls._instance
    return inner


@single
class SingleClass(object):
    def __init__(self):
        pass

single3 = SingleClass()
single4 = SingleClass()

print(id(single3) == id(single4))