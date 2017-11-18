t = int(input())
while t :
    n = int(input())
    s = 0
    k = 0
    for i in range(n):
        line = [float(i) for i in input().split()]
        s += line[0]*line[1]
        k += line[0]
    print(int(k),round(s/k,1))
    t-=1
