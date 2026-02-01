"""
实例068：旋转数列
题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
"""

from collections import deque

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr)

deq = deque(arr, maxlen=len(arr))
rotate = 3
deq.rotate(rotate)
print(list(deq))
