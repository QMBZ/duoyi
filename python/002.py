"""
实例002：“个税计算”
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
"""

# 提成规则
commission_rules = [
    (10, 0.1),
    (20, 0.075),
    (40, 0.05),
    (60, 0.03),
    (100, 0.015),
    (float("inf"), 0.01),  # 100w以上
]

# 利润
profit = 2.223125

if profit < 0:
    print("利润必须大于0")
else:
    total_bonus = 0  # 总提成
    prev_threshold = 0  # 上一个区间的下限，初始为0

    # 遍历
    for threshold, rate in commission_rules:
        if profit <= prev_threshold:
            # 如果利润小于这个，那么就计算完毕了
            break

        # 计算利润
        current_profit = min(profit, threshold) - prev_threshold
        # 累加提成
        total_bonus += current_profit * rate
        # 更新区间下限
        prev_threshold = threshold

# 输出
print(f"利润：{profit}w")
print(f"提成：{total_bonus:.6f}w")
