def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        ret = yield a  # 如果一个函数中有yield语句， 那么这个就不再是函数， 而是一个生成器的模板
        print(ret)
        a, b = b, a+b
        current_num += 1


# 如果在调用create_num的时候，发现这个函数中有yield那么此时，不是调用函数， 而是创建一个生成器。
obj = create_num(10)

ret = next(obj)
print(ret)

ret = obj.send("hahaha")  # 传递的值 作为yield的结果, 不能作唯第一次启动， 如果使用可以使用None
print(ret)
