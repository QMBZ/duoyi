"""
实例043：作用域、类的方法与变量
题目：模仿静态变量(static)另一案例。
"""


class sim:
    num = 0

    def add_num(self):
        print(f"class num: {self.num}")
        print(f"global num: {num}")
        self.num += 1


n = sim()
num = 0
for i in range(10):
    num *= 2
    n.add_num()
