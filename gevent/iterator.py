import time
from collections import Iterable
from collections import Iterator


class Classmate(object):
    """
        this is a iterator
    """
    def __init__(self):
        self.names = list()
        self.current_num = 0
    
    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration


classmate = Classmate()
classmate.add("1")
classmate.add("2")
classmate.add("3")

print("判断classmate是否是可以迭代的对象：", isinstance(classmate, Iterable))
print("判断classmate是否是迭代器：", isinstance(classmate, Iterator))


for data in classmate:
    print(data)