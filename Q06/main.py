def f(inputNum,B):
    isPal=0
    while inputNum:
        inputNum,isPal=inputNum/B,isPal*B+inputNum%B
    return isPal 
for tc in range(int(input())):
    n=int(input())
    result=0
    for i in range(2,65):
        if n==f(n,i):
            result=1
    print (result)
