n, k = map(int,input().split())
res = []
target=0
for i in range(n):
    a, *b = map(int,input().split())
    if a == k:
        target = b
    res.append(b)
print(res)
res.sort(reverse=True)
print(res.index(target)+1)
