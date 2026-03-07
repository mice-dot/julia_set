# test_log_decorator.py

"""
pytest 測試 log_decorator
"""

from log_decorator import add


def test_add_result():
    """
    測試 add 回傳值
    """

    result = add(2, 3)

    assert result == 5


def test_add_name():
    """
    測試 wraps 是否保留名稱
    """

    assert add.__name__ == "add"


def test_add_doc():
    """
    測試 wraps 是否保留 docstring
    """

    assert add.__doc__ == "加法函式"
