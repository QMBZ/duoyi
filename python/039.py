"""
实例039：有序列表插入元素
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
"""

# arr = [1, 10, 100, 1000, 10000, 100000]
arr = [100000, 10000, 1000, 100, 10, 1]
num = 33

if arr and arr[0] <= arr[-1]:  # 升序
    for i, x in enumerate(arr):
        if num <= x:
            arr.insert(i, num)
            break
    else:
        arr.append(num)
else:  # 降序
    for i, x in enumerate(arr):
        if num >= x:
            arr.insert(i, num)
            break
    else:
        arr.append(num)

print(arr)
