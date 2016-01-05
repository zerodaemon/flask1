# coding=utf-8
def decorator_maker():
    print "装饰器创造者开始!"

    def my_decorator(func):
        print "装饰器开始包装函数"

        def wrapped():
            print ("我就是那个包装，包装以后的函数每次运行都有我"
                   "作为包装函数，我返回的是结果")
            return func()

        print "包好了！"
        return wrapped

    print "装饰器已经生成！"
    return my_decorator


@decorator_maker()
def decorated_function():
    print "苹果苹果和苹果"

decorated_function()