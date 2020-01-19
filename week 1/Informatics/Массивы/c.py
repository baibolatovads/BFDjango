n = int(input())
arr = []
inp = input().split()
for i in range(0, n):
  arr.append(int(inp[i]))

cnt = 0

for l in range(0, len(arr)):
	if arr[l] > 0: 
    	  cnt += 1
print(cnt)