n, k = map(int, input().split())
coins = [int(input()) for i in range(n)]
d=[[0 for i in range(100001)] for i in range (n)]
for i in range (n) : d[i][0] =1
for i in range(n):
    print(d[i][0:k+1])

for i in range(n) :
    for j in range (1,k+1):
        if j >= coins[i]:
            d[i][j] = d[i-1][j-coins[i]] + d[i-1][j]
        else : 
            d[i][j] = d[i-1][j]
    print (d[i-1][0:k+1])
for i in range(n):
    print(d[i][0:k+1])
print(d[n-1][k])
