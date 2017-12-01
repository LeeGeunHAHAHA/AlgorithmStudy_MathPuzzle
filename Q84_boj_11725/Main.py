from collections import deque as queue
N = int(input())
cnj = [[] for i in range (N)]
depth= [ 0 for i in range(N)]
for i in range (N-1) :
    a, b = map(lambda x : int(x) -1, input().split())
    cnj[a].append(b)
    cnj[b].append(a)
q = queue()
def BFS(root):
    q.append((1,cnj[root]))
    depth[root] = 1
    while q :
        d , nexts = q.popleft()
        for i in nexts :
            if depth[i] == 0 :
                depth[i] = d+1
                q.append((d+1,cnj[i]))
BFS(0)
for i in range(1,N):
    index = depth[i]
    for j in cnj[i]:
        if depth[j] < index:
            print(j+1)

        

