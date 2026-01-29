"""
实例025： 阶乘求和
题目：求1+2!+3!+...+20!的和。
"""

result = 1
for i in range(3, 1, -1):
    result = i * result + 1
print(result)
