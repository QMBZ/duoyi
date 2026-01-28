"""
实例009：暂停一秒输出
题目：暂停一秒输出
"""

import time

for i in range(1, 10):
    print(i, time.time())
    time.sleep(1)
