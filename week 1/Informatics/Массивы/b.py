n = int(input())
arr = []
inp = input().split()
for i in range(0, n):
  arr.append(int(inp[i]))

for l in range(0, len(arr)):
	if arr[l] % 2 == 0: 
    	  print(arr[l])