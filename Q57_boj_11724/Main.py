#!/usr/bin/env/python
maps = [[]]
visit= [0]
v =0
e =0
cnt = 0
def getGraph() :
    v , e = [int(i) for i in input().split()]
    for i in range(v):
        maps.append([])
        visit.append(False)
    for i in range (e) :
        a , b =[int(i) for i in input().split()]
        maps[a].append(b)
def dfs(node):
    if visit[node] == True : return 
    visit[node] = True
    for i in maps[node] :
        dfs(i)
    
if __name__=="__main__":
    getGraph()
    for i in maps :
        if i ==[] :
            continue
        if visit[i[0]] == False:    
            cnt +=1
            dfs(i[0])
    print(cnt)



