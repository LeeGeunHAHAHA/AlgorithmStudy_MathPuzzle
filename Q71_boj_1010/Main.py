t = int(input())
d=list()
while t:
    m ,n = map(int,input().split())
    d = [[0 for i in range(m+1)]  for j in range(n+1)]
    for j in range (1,m+1):
        for i in range(1, n+1):
            print(d[i][j], end = " " )
        print("") 
    t-=1
