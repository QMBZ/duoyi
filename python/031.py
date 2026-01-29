"""
实例031：字母识词
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
"""

# 第一个字母相同的有 t: 周二周日，s: 周六周天
# 所以要额外处理一下
week_t = {"u": "Tuesday", "h": "Thursday"}
week_s = {"a": "Saturday", "u": "Sunday"}
weeks = {
    "t": week_t,
    "s": week_s,
    "m": "Monday",
    "w": "Wednesday",
    "f": "Friday",
}

first = "s"
second = "a"
week = weeks[first]

if week == week_s or week == week_t:
    print(week[second])
else:
    print(week)
