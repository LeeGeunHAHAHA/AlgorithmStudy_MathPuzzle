def cal(n,d):
    if n ==1 : return True
    if d.__contains__(n): return False
    t = n
    nextN = 0
    while t>0 :
        nextN += int(pow((t%10),2))
        t //=10
    d.setdefault(n,1)
    return cal(nextN,d)



if __name__=="__main__":
    
    t = int(input())
    for i in range (t):
        d ={}
        n = int(input())
        if cal(n,d) : print("HAPPY")
        else : print("UNHAPPY")

