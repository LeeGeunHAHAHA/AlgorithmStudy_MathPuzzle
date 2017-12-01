n = int(input())
target = [int(i) for i in input().split()]
dp = [1 for i in range(n)]
dpr = [1 for i in range(n)]
for i in range (1,n):
    tmp =[]
    for j in range (0,i):
        if target[j] < target [i] :
            tmp.append(dp[j])
        if tmp != []: dp[i] = 1 + max(tmp)
target.reverse()
for i in range (1,n):
    tmp =[]
    for j in range (0,i):
        if target[j] < target [i] :
            tmp.append(dpr[j])
        if tmp != []: dpr[i] = 1 + max(tmp)
dpr.reverse()
#print(dp)
#print(dpr)
ans = [dp[i]+dpr[i] for i in range(n)]
#print(ans)

print(max(ans)-1)
