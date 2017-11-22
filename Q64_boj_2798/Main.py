import copy.deepcopy
c, ub = map(int, input().split())
cards = list(map(int, input().split()))

def cal(idx,target) :
    if idx ==3 :
        for i in target :
            return i
    t = target 
    for i in range(len(t)) : 
        p =t.pop(i)
        cal(idx+1,t)
        t.(i,p)
    
    
