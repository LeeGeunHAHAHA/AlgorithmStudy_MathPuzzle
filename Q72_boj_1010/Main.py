t = int(input())
# cal in top down  -> no memoiztion
while t :
    def cal(m,n):
        print(m,n)
        if m==n : return 1
        if m ==1 :
            return n;
        ans = 0
        for i in range (n-1,m-2,-1) :
           ans += cal(m-1,i)
        return ans
    a,b = map(int, input().split())
    #print(cal(a,b))
    d=[[1 for i in range (b+1)] for j in range(a+1)]

    #print (d)
    for i in range (1,a+1) :
        for j in range(1,b+1):
            if i ==j :
                d[i][j] = 1
            if i==1 :
                d[i][j] = j
            else :
                for k in range(i,j):
                    d[i][j] += d[i-1][k]

    #print(d)
    print(d[a][b])
    t-=1
