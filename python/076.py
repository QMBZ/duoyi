"""
实例076：做函数
题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
"""


def even_add(n):
    sum = 0.0
    for i in range(2, n + 1, 2):
        sum += 1.0 / i
    return sum


def odd_add(n):
    sum = 0.0
    for i in range(1, n + 1, 2):
        sum += 1.0 / i
    return sum


def call_add(fun, n):
    sum = fun(n)
    return sum


if __name__ == "__main__":
    n = 4
    if n % 2 == 0:
        sum = call_add(even_add, n)
    else:
        sum = call_add(odd_add, n)
    print(sum)
