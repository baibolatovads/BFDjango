import math
a = int(input())
b = int(input())
res = abs(a * b) % 109

if a > 0:
	c = res % 109
else:
	c = (109 - res) % 109

print(c)