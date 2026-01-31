"""
实例042：变量作用域
题目：学习使用auto定义变量的用法。
"""

i = 0
n = 0


def fun_1():
    i = 0
    print(i)
    i += 1


def fun_2():
    global n
    print(n)
    n += 1


for i in range(10):
    print(i)
    fun_1()
    i += 1

for j in range(10):
    print(n)
    fun_2()
    n += 2
