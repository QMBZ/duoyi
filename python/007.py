"""
实例007：copy
题目：将一个列表的数据复制到另一个列表中。
"""

import copy

a = [1, 2, 3, 4, ["a", "b"]]

b = a  # 赋值
c = a[:]  # 浅拷贝
d = copy.copy(a)  # 浅拷贝
e = copy.deepcopy(a)  # 深拷贝

a.append(5)
a[4].append("c")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"d = {d}")
print(f"e = {e}")
