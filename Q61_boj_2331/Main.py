n , p = [int(i) for i in input().split()]
def cal(x):
    s = 0
    while(x) :
        s+= int(pow(x%10,p))
        x//=10
    return s
d = dict()
d.update({n:1})
ans = 0
while 1 :
    prv = n
    n = cal(n)
    if d.__contains__(n) :
        ans = d[n] -1
        print(ans)
        break
    else :
        d.setdefault(n,d[prv] +1)
