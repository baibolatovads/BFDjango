n = int(input())
arr = []
inp = input().split()
for i in range(0, n):
  arr.append(int(inp[i]))

for l in range(0, len(arr), 2):
    print(arr[l])