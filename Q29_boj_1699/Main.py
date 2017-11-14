import math as m
import sys
sys.setrecursionlimit(1000000)

def root(t):
    return int(m.sqrt(t))

d = [0 for i in range(100001)]

def cal(n) :
    if d[n] != 0 : return d[n]
    r = root(n)
    if n == pow(r,2):
        d[n] = 1
        return 1
    ans = cal(n-1) + cal(1)
    for i in range (2,r+1):
        if d[i*i] != 0:
            tmp = cal(n-i*i) + d[i*i]
        tmp = cal(n-i*i) + cal(i*i)
        if ans > tmp:
            ans = tmp
    d[n] = ans
    return ans
n = int(input())
ans =cal(n)
print(ans)
        
