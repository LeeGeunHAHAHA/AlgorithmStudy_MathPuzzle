from collections import deque as queue
n = int()
m = int()
cnt = int()
q = queue()
dx=[1,0,-1,0,1,1,-1,-1]
dy=[0,1,0,-1,1,-1,1,-1]
def isInRange(x,y):
    return x>=0 and x <m and y >=0 and y<n
def BFS(x,y):
    q.append((x,y))
    while q :
        tx, ty =q.popleft();
        land[tx][ty] = 0
        for i in range (8):
            nx = tx+dx[i]
            ny = ty+dy[i]
            if isInRange(nx,ny) and land[nx][ny]: q.append((nx,ny))
    return


while (1):
    n,m = map(int,input().split())
    q.clear()
    cnt =0
    if not m and not n : break
    land = [[int(i)for i in  input().split() ]for i in range(m)]
    for i in range(n) :
        for j in range(m) :
            if land[j][i] :
                BFS(j,i)
                cnt+=1
    print(cnt)
