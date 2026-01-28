"""
实例014：分解质因数
题目：将一个整数分解质因数。例如：输入90,打印出90=2*3*3*5。
"""


# 质因数分解
def prime_factors(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"

    # 是否是负数
    is_negative = n < 0
    n = abs(n)
    # 记录原始值，方便后面输出
    original_n = n

    # 质因子数组
    factors = []

    # 先处理2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # 处理奇数
    i = 3
    while i * i < n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2

    # 如果还有剩下的，那就是其他质数了
    if n > 1:
        factors.append(n)

    # 剩下的就是输出了
    if is_negative:
        result = ["-1"] + [str(f) for f in factors]
    else:
        result = [str(f) for f in factors]

    if is_negative and factors:
        return f"-{original_n} = " + "x".join(result)
    elif is_negative:
        return f"-{original_n} = -1"
    else:
        return f"{original_n} = " + "x".join(result)


target = 11190
print(prime_factors(target))
