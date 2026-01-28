"""
实例010：给人看的时间
题目：暂停一秒输出，并格式化当前时间。
"""

import time

for i in range(1, 10):
    current_time = time.localtime(time.time())

    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
    print(f"{i}: {formatted_time}")
    time.sleep(1)
