"""
实例018：复读机相加
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
"""

a = "7"
n = 7
result = 0
for i in range(n):
    print(a, end=" ")
    result += int(a)
    a += a[0]

print(result)
