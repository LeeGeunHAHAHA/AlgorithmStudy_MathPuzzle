import sys
sys.setrecursionlimit(100000000)
n=int(input())

dp=[0,1]
dm=[0,1]
flag=0
def fib(n):
    if n >= 0 and len(dp) > n:
        return dp[n]
    if n < 0 and len(dm) > -n :
        return dm[-n]
    if n >= 0 :
        ret = fib(n-1) + fib(n-2)
        dp.append(ret)
    if n < 0 :
        ret = fib(n+2)-fib(n+1)
        dm.append(ret)
    return ret
if n> 0 : flag = 1
if n <0:
    n = -n
    flag = -1
if flag == 0 : print(0)
if n> 0:
    a=0
    b=1
    c=0
    for i in range(0,n):
        c= a+b
        a =b
    print(flag)
    if flag == -1 and n %2==0 :
        print(-(c%1000000000))
    else : print (c%1000000000)
print(fib(n)%1000000000)
        
