# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 14:18:59 2025

@author: jos
"""
import time
from functools import wraps

if 'line_profiler' not in dir() and 'profile' not in dir():
    def profile(func):
        @wraps(func)
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner


@profile
def list_append(y, y1, i = 1000):
    for o in range(i):
        y.append(y1)
        time.sleep(0.002)
    return y


def main():
    y = [x for x in range(10)]
    y1 = [x for x in range(5)]
    print(y)
    print(y1)
    y = list_append(y, y1, 1000)
    print(y[:40])


if __name__ == "__main__":
    main()
