"""
实例004：这天第几天
题目：输入某年某月某日，判断这一天是这一年的第几天？
"""


# 判断是否是闰年
def is_leap_year(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)


# 每月之前总共多少天
days_before_month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]


# 计算今天是这年的第几天
def day_of_year(date):
    # 解包yuan'zu
    year, month, day = date
    # 先按照非闰年计算
    total = days_before_month[month - 1] + day

    # 再判断是否是闰年且月份是否大于2月
    if is_leap_year(year) and month > 2:
        total += 1

    return total


date = (2026, 2, 22)
print(day_of_year(date))
