import queue
visit =[]
graph = []
data = input().split()
node = int(data[0])
edge = int(data[1])
start= int(data[2])
q = queue.Queue()

def getInput():
    global graph,visit, data, node, edge
    for i in range(0,node):
        graph.append([])
        visit.append(False)
    for i in range (0,edge):
        data= input().split()
        startNode = int(data[0])-1
        nextNode = int(data[1])
        graph[startNode].append(nextNode)
        graph[nextNode-1].append(startNode+1)
        graph[startNode].sort()
        graph[nextNode-1].sort()
def dfs(num):
    print(num, end="")
    global visit,graph
    visit[num-1]=True
    for i in graph[num-1]:
        nextNum = i
        if visit[nextNum-1] == False:
            print(" ", end="")
            dfs(nextNum)
    return 
def bfs(num):
    global graph, visit, q
    q.put(num)
    visit[num-1] =False
    while(not q.empty()):
        now = q.get() -1
        if now == num-1:
            print(str(now+1),end="")
        else :
            print(" "+str(now+1),end="")
        for i in graph[now]:
            if(visit[i-1]==True):
                q.put(i)
                visit[i-1] =False

if __name__ == "__main__" :
    getInput()
    dfs(start)
    print("")
    bfs(start)
