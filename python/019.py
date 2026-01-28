"""
实例019：完数
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
"""


def get_factors(n):
    factors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            # 再加上另一个因子
            if i != n // i:
                factors.append(n // i)
        i += 1
    return factors


for i in range(1000):
    factors = get_factors(i)
    if sum(factors) - i == i:
        print(i)
