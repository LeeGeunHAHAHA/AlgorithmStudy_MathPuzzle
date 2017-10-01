def getInput():
    n = int(input())
    line = input().split()
    inputList = [int(i) for i in line]
    return inputList
def cal(ducci):
    if containSame(ducci) : return True
    if len(ducci)%2 ==1 : return False
    dcpocket=[]
    dcpocket.append(ducci)
    l= len(ducci)
    while 1 :
        ducci = dcpocket[-1]
        newDucci=[]
        for i in range (0,l):
                newDucci.append(abs(ducci[i]-ducci[-l+i+1]))
        if containSame(newDucci) :return True
        try:
            if dcpocket.index(newDucci) : return False
        except :
            dcpocket.append(newDucci)
def containSame(ducci):
    a = ducci[0]
    for i in ducci:
        if i != a : return False
    return True
if __name__ == "__main__":
    testCase = int(input())
    while testCase:
        a = getInput()
        if cal(a) : print ("ZERO")
        else : print("LOOP")
        testCase-=1
