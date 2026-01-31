"""
实例047：函数交换变量
题目：两个变量值用函数互换。
"""


def i_swap(a, b):
    return (b, a)


a = 0
b = 10
print(f"a = {a}, b = {b}")
a, b = i_swap(a, b)
print(f"a = {a}, b = {b}")
