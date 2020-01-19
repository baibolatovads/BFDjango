x = int(input())
k = 0
for i in range(1, x + 1):
	if x % i == 0:
		k = k + 1

print(k)