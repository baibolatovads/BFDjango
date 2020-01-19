from collections import Counter

shoes = int(input())
arr = map(int,input().split())
customer = int(input())
n = Counter(arr)
res = 0
lst = map(tuple,(map(int,input().split()) for _ in range(customer)))
for i in lst:
    if i[0] in n.keys() and n[i[0]] >0 :
        n[i[0]] = n[i[0]]-1
        res = res+i[1]
print(res)