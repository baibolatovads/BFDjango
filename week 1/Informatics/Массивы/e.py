n = int(input())
arr = []
inp = input().split()
for i in range(0, n):
  arr.append(int(inp[i]))

found = False

for l in range(0, len(arr) - 1):
	if arr[l] * arr[l + 1] > 0: 
    	  found = True

if found == True:
	print("YES")
else:
	print("NO")