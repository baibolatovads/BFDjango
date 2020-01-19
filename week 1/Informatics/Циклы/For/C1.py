import math

a = int(input())
b = int(input())

[print(x * 2,end = " ") for x in range(math.ceil(a * 0.5), math.floor(b ** 0.5) + 1)]