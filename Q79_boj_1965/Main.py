n = int(input())
nums = [int(i) for i in input().split()]
dp = [1 for i in range(n)]
for i in range (1,n):
    for j in range(0,i):
        if nums[i] > nums[j]:
            dp[i] = 1 +dp[j] if dp[i] <dp[i]+1 else dp[i] 
print(sorted(dp)[-1])
