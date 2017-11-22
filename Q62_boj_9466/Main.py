import sys
sys.setrecursionlimit(100000000)
cnt = 0
m = dict()
stNum= 0
cnj = None
visit = None

def getInput():
    global cnj,visit ,stNum
    stNum= int(input())
    cnj = list();visit = list()
    for i in range (stNum):
        visit.append(0)
        cnj.append([])
    inputs = [int(i)-1 for i in input().split()]
    for i in range (stNum) :
        cnj[i].append(inputs[i])
def dfs(curNd,dfsN,ndCnt):
    global cnt
    if visit[curNd] !=0 :
        if visit[curNd]!=dfsN : return
        cnt += ndCnt - m[curNd]
        return
    visit[curNd] = dfsN
    m.setdefault(curNd,ndCnt)
    dfs(cnj[curNd][0],dfsN,ndCnt+1)
    m.clear()

if __name__ == "__main__" :
    t = int(input())
    while t :
        getInput()
        for i in range (stNum):
            if visit[i] == 0:
                dfs(i,i+1,1)
        print(stNum-cnt)
        cnt=0
        
        t-=1
    


