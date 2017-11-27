numOfCoin , target = map(int,input().split())
coins = [int(input()) for i in range (numOfCoin)]
d = [ 0 for i in range (10001)]
d[0] =1

for i in range (0, numOfCoin):
    for j in range (1,target+1):
        if j >= coins[i] :
            d[j] += d[j-coins[i]]
    #print(d[0:11])
print(d[target])
