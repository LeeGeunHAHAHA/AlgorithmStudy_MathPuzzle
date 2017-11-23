from collections import deque as queue 
v =int(input()); e = int(input())
cnj =[[] for i in range(v)]
visit = dict()
q = queue()
for i in range (v) : visit.setdefault(i,0)
for i in range(e) :
    cur , nex = map(lambda x : int(x)-1 ,input().split())
    cnj[cur].append(nex)
    cnj[nex].append(cur)
def bfs(cur,idx) :
    global visit
    q.append(cur)
    visit[cur] =idx
    cnt = idx
    while(q):
        nex= q.popleft()
        cnt = visit[nex]+1
        for i in cnj[nex] : 
            if visit[i] == 0:
                q.append(i)
                visit[i] = cnt
bfs(0,1)
#print(cnj)
#print(visit)
a = list(map(lambda x:1 if x>1 and x<4 else 0  ,visit.values()))
print(sum(a))




