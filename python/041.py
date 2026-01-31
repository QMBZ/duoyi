"""
实例041：类的方法与变量
题目：模仿静态变量的用法。
"""


def a_n():
    i = 0
    print(i)
    i += 1


class sim:
    i = 0

    def a_n(self):
        print(self.i)
        self.i += 1


a = sim()
for i in range(10):
    a_n()
    a.a_n()
