def my_decorator(func):
    """這是 decorator 函式"""
    def wrapper():
        """這是 wrapper 函式"""
        print("函式開始執行")
        func()
        print("函式執行結束")
    return wrapper

@my_decorator
def hello():
    """這是 hello 函式"""
    print("Hello Python")

hello()
print(hello.__name__)
print(hello.__doc__)
