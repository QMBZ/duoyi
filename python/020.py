"""
实例020：高空抛物
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
"""


def calculate_distance(n):
    height = 100

    # 总距离 = 第一次下落 + 后续的反弹+下落
    # 第i次反弹高度 = 100/2^i
    # 总距离 = 100 + 2 * (100/2 + 100/4 + ... + 100/2^(n-1))

    # 第一次下落
    total_distance = height

    # 后续的反弹+下落
    for i in range(1, n):
        total_distance += 2 * height / (2**i)

    # 第n次反弹高度
    last_height = height / (2**n)

    return total_distance, last_height


n = 10
total, last = calculate_distance(n)
print(f"第{n}次落地时，共经过{total}米")
print(f"第{n}次反弹高度为{last}米")
