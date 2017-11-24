n = int(input())
house =[]
house.append([0,0,0])
for i in range(n+2):
    tmp=list(map(int,input().split()))
    house.append(tmp)
d =[[0,0,0] for i in range(n+1)]
d[0] =[0,0,0]
for i in range (1,n+1):
    for j in range (3):
        d[i][j] = min(d[i-1][(j+1)%3],d[i-1][(j+2)%3])+house[i][j]
print(min(d[n]))
