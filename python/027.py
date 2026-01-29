"""
实例027：递归输出
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
"""


def rec(string):
    if len(string) != 1:
        rec(string[1:])
    print(string[0], end="")


rec("12345678")
