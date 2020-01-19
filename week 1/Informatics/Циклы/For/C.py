import math
a = int(input())
b = int(input())

for i in range(math.sqrt(a), math.sqrt(b + 1)):
	if (int(i * i) >= a and int(i * i) <= b):
		print(str(i * i))