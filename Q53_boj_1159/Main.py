n = int(input())

ans =""
d = dict()
for i in range(n):
    f = input()[0]
    if d.__contains__(f):
        d[f] += 1
    else : d.setdefault(f,1)
tmp = sorted(list(map(lambda x : x if d[x]>=5 else "",d.keys())))
for i in tmp :
    ans+=i
if ans == "":
    print("PREDAJA")
else :print(ans)
