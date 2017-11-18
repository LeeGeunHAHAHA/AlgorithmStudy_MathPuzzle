d = dict()
for i in range (8) :
    d.update({int(input()):i})
tmp = sorted(d.keys(), reverse = True)
print(sum(tmp[:5]))
ans = []
for i in range(5):
    ans.append(d[tmp[i]]+1)
for i in sorted(ans) :
    print(i,end=" ")
    

