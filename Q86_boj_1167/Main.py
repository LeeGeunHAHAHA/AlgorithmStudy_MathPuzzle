n = int(input())
cnj =[[] for i in range (n)]
visit= [False for i in range(n)]
sums = []
for i in range (n) :
    line = [int(i) for i in input()[:-2].split()]
    t = line.pop(0)-1
    for j in range(0,len(line)-1,2):
        cnj[t].append((line[j],line[j+1]))
def DFS (node,s): 
    if visit[node] :return
    visit[node] = True
    for i in cnj[node]:
        DFS(i[0]-1,i[1]+s)
    sums.append((s,node))
visit= [False for i in range(n)]
DFS(0,0)
visit= [False for i in range(n)]
start = (max(sums))
DFS(start[1],0)       
print(max(sums)[0])
    
