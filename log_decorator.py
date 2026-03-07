# log_decorator.py

"""
此模組示範 decorator 與 wraps 使用
"""

from functools import wraps


def log_decorator(func):
    """
    log decorator

    用來記錄函式執行
    """

    # wraps 保留 func 原始資訊
    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"呼叫函式：{func.__name__}")

        result = func(*args, **kwargs)

        print(f"函式完成：{func.__name__}")

        return result

    return wrapper


@log_decorator
def add(a, b):
    """加法函式"""
    return a + b

print(add(5, 9))
print(add.__name__)
print(add.__doc__)
