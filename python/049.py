"""
实例049：lambda
题目：使用lambda来创建匿名函数。
"""

MAX = lambda x, y: x * (x >= y) + y * (y > x)
MIN = lambda x, y: x * (x <= y) + y * (y < x)

a = 1
b = 2

print(MAX(a, b))
print(MIN(a, b))
