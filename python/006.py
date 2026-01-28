"""
实例006：斐波那契数列
题目：斐波那契数列。
"""


def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]

    fib_sequence = [1, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


n = 10
fib_seq = fibonacci_iterative(n)
print(fib_seq)
