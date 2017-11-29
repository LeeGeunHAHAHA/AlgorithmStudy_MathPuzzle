m ,n = map(int, input().split())
maps = [[int(i) for i in input().split()] for i in range(m)]
dx = [-1,0,-1]
dy = [0,-1,-1]
def isSafe(x,y):
    return x>= 0 and y>=0 and x<m and y<n
for i in range(0,m):
    for j in range (0,n):
        tmp =[]
        for k in range(3):
            nx = i+dx[k]
            ny = j+dy[k]
            if isSafe(nx,ny) :
                tmp.append(maps[nx][ny])
        if tmp != [] : maps[i][j] += max(tmp)
            
print(maps[m-1][n-1])

        
            

