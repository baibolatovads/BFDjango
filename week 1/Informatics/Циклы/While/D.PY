n = int(input())
i = 0
while n>0:
	i += n%2
	n = n//2

if i == 1:
	print("YES")
else: 
	print("NO")	

