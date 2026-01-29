"""
实例023：画菱形
* *** ***** ******* ***** *** *
"""


def draw(n):
    max_width = 2 * n - 1

    for i in range(1, n + 1):
        stars = "*" * (2 * i - 1)
        print(stars.center(max_width))

    for i in range(n - 1, 0, -1):
        stars = "*" * (2 * i - 1)
        print(stars.center(max_width))


draw(5)
