"""
实例017：字符串构成
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""

string = "lsalldas 啦大啦爱了就爱收到 12131312  😋"
alp = 0
num = 0
spa = 0
oth = 0
for i in range(len(string)):
    if string[i].isspace():
        spa += 1
    elif string[i].isdigit():
        num += 1
    elif string[i].isalpha():
        alp += 1
    else:
        oth += 1
print(f"space: {spa}")
print(f"digit: {num}")
print(f"alpha: {alp}")
print(f"other: {oth}")
