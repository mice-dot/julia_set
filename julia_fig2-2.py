# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 10:57:50 2026

@author: jos
"""

import matplotlib.pyplot as plt

def julia(i = 50, z = 0 + 0j , c = -0.62772 - 0.42193j):
    y = []
    for n in range(i):
        z = z * z + c
        abs_z = abs(z)
        y.append(abs_z)
        print(f"{n}: z={z: .5f}, abs(z)={abs_z:0.3f}, c={c: .5f}")
    return y

y = julia()
x = [i+1 for i in range(len(y))]
plt.plot(x, y, label="z = 0 + 0j")
y = julia(10, -0.82 + 0j)
x = [i+1 for i in range(len(y))]
plt.plot(x, y, label="z = -0.82 + 0j", marker='o')
plt.title("Julia set f=z*z+c, c = -0.62772 - 0.42193j")
plt.xlabel("Number of iterations")
plt.ylabel("abs(z)")
plt.grid(True)
plt.legend() # 需要下該指令label才會顯示出來
plt.show() # 顯示所有figure