n = int(input())
d = [0,1,1]
for i in range (3,80):
    d.append(d[i-2]+d[i-1])
if n >= 4 :
    print((d[n-2]+2*d[n-1]+d[n])*2)
if n == 1:
    print(4)
if n ==2 :
    print (6)
if n==3 :
    print(10)
