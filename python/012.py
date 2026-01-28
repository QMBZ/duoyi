"""
实例012:100到200的素数
题目：判断101-200之间有多少个素数，并输出所有素数。
"""


# 判断质数
def is_prime(n):
    if n <= 1:
        # 1 不是质数
        return False
    if n <= 3:
        # 2 和 3 是质数
        return True
    if n % 2 == 0 or n % 3 == 0:
        # 如果能被 2 和 3 整除，不是质数
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


for i in range(201):
    if is_prime(i):
        print(i)
