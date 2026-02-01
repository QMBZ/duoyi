"""
实例069：报数
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
"""

n = 3
people = list(range(1, n + 1))

index = 0
count = 0
while len(people) > 1:
    count += 1  # 报数
    if count == 3:
        # 移除人
        people.pop(index)
        count = 0  # 重新报数
    else:
        index = (index + 1) % len(people)

print(people[0])
