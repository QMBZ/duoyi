"""
实例044：矩阵相加
题目：计算两个矩阵相加。
"""

x = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]

y = [[5, 8, 1], [6, 7, 3], [4, 5, 9]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(result)):
    for j in range(len(result[0])):
        result[i][j] = x[i][j] + y[i][j]
print(result)
