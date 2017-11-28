t = int(input())
while t :
    n = int(input())
    stc = [[int(i) for i in input().split() ]for i in range (2)]
    d = [[0 for i in range(n) ]for i in range (2)]
    d[0][0]=stc[0][0]
    d[1][0]=stc[1][0]
    d[0][1]=stc[0][1] + stc[1][0]
    d[1][1]=stc[1][1] + stc[0][0]
    for i in range (2, n) :
            d[1][i] = max(d[0][i-1]+stc[1][i],d[0][i-2]+stc[1][i])
            d[0][i] = max(d[1][i-1]+stc[0][i],d[1][i-2]+stc[0][i])
    print(max(d[1][n-1],d[0][n-1]))

    t-=1

