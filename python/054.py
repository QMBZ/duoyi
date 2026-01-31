"""
实例054：位取反、位移动
题目：取一个整数a从右端开始的4〜7位。
"""

a = 12345
b = 0  #     0
b = ~b  #     1
b = b << 4  # 10000
b = ~b  #  1111
c = a >> 4
d = c & b
print(f"a:{bin(a)}")
print(f"b:{bin(b)}")
print(f"c:{bin(c)}")
print(f"d:{bin(d)}")
