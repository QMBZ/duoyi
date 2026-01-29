"""
实例033：列表转字符串
题目：按逗号分隔列表。
"""

arr = [1, 2, 3, 4, 5]
print(",".join(str(n) for n in arr))
