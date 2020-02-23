class Subject(object):
    def __init__(self):
        # 观察者注册的列表
        self.__observers = []
    
    def register(self, observer):
        self.__observers.append(observer)
        print("添加新观察者！%s" % type(observer).__name__)
    
    def remove(self, observer):
        if len(self.__observers) != 0:
            self.__observers.remove(observer)

    def notifyAll(self, *args):
        for observer in self.__observers:
            observer.notify(self, *args)
    

class Observer(object):
    def notify(self, subject, *args):
        raise NotImplementedError()

class TestData1(Observer):
    def __init__(self, subject):
        subject.register(self)
    
    def notify(self, subject, *args):
        print("%s 从对象 %s 处 得到通知：%s" %
         (type(self).__name__, type(subject).__name__, args))

class TestData2(Observer):
    def __init__(self, subject):
        subject.register(self)
    
    def notify(self, subject, *args):
        print("%s 从对象 %s 处 得到通知：%s" %
         (type(self).__name__, type(subject).__name__, args))


subject = Subject()
observer1 = TestData1(subject)
subject.notifyAll("测试数据1！")
observer2 = TestData2(subject)
subject.notifyAll("测试数据2！")




