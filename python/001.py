"""
实例001：数字组合
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""

# 普通方法
total = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                total += 1
print(total)


# 使用 itertools
# import itertools

# total = 0
# nums = [1, 2, 3, 4]
# for i in itertools.permutations(nums, 3):
#     total += 1
# print(total)
