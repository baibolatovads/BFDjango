def Xor(x, y):
	if x == 0 and y == 1:
		return true
	if x == 1 and y == 0:
		return true
return false

a, b = [bool(x) for x in input().split()]
Xor(a, b)