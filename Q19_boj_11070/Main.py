t = int(input())
while t :
    n,m =map(int,input().split())
    teams =[[0.0,0.0] for i in range(n)]
    for i in range (m):
        a,b,w,l=[int(i) for i in input().split()]
        teams[a-1][0]+= w
        teams[a-1][1]+= l
        teams[b-1][0]+= l
        teams[b-1][1]+= w
    ans=[]
    for i in teams:
        W=i[0]
        S=i[1]
        if not W and not S:
            ans.append(0)
            continue
        w=pow(W,2)
        s=pow(S,2)
        ans.append((w/(w+s))*1000)
    ans.sort()
    print(int(ans[-1]))
    print(int(ans[0]))
    


    t-=1
