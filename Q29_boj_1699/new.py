from math import sqrt
n = int(input())
dp =[ i for i in range(100001)]
for i in range (2,n+1):
    for j in range(2,i):
        if j*j>i: break
        dp[i] = min(dp[i], 1+dp[i-j*j])
print(dp[n])
