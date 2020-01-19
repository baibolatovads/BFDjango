n = int(input())
arr = []
inp = input().split()
for i in range(0, n):
  arr.append(int(inp[i]))

cnt = 0

for l in range(0, len(arr) - 1):
	if arr[l + 1] > arr[l]: 
    	  cnt += 1
print(cnt)