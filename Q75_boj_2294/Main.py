n,k = map(int,input().split())
coins = [ int(input()) for i in range (n)]

dp = [0 for i in range (100001) ]
# dp[0]  =1 
for i in  coins : dp[i] = 1
for i in range (1,k+1):
    for j in coins :
        if i > j and dp[i-j] :
            cnd = dp[i-j]+1
            if not dp[i] : dp[i] = cnd
            else : dp[i] = cnd if cnd<dp[i] else dp[i]

print(dp[k] if dp[k] else -1)
