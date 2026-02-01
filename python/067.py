"""
实例067：交换位置
题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
"""

arr = [3, 2, 5, 7, 8, 1, 5]
print(arr)

max_index = arr.index(max(arr))
min_index = arr.index(min(arr))

arr[0], arr[max_index] = arr[max_index], arr[0]
arr[-1], arr[min_index] = arr[min_index], arr[-1]
print(arr)
