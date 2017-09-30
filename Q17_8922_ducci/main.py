def getInput():
    n = int(input())
    line = input().split()
    if isAllSame(line) : return True
    a =[int(i) for i in line]
    return calc(a)
def calc(ducci):
    print(ducci)
    l= len(ducci)
    if l%2==1: return False 
    if isAllSame(ducci): return True
    for i in range(0,l+1):
        ducci[i-l] = abs(ducci[i-l]-ducci[i+1-l])
    return calc(ducci)
def isAllSame(ducci):
    a=ducci[0]
    for i in ducci:
        if i!=a: return False
    return True

# start of main
if __name__ =="__main__":
    testCase =0
    testCase = int(input())
    while testCase!=0:
        if getInput(): print("ZERO")
        else : print("LOOP")
        testCase-=1
