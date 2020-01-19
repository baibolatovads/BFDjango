x = int(input())

a = x % 4
b = x % 100
c = x % 400

if (a == 0 and b != 0) or c == 0:
	print("YES")
else:
	print("NO")