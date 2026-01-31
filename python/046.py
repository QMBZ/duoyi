"""
实例046：打破循环
题目：求输入数字的平方，如果平方运算后小于 50 则退出。
"""

i = 1

while True:
    if i * i < 50:
        print(i * i)
        i += 1
        continue
    else:
        break
