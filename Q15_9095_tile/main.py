d=[]
d.append(0)
d.append(1)
d.append(3)
for i in range(3,1001):
    d.append(d[i-1]+2*d[i-2])
n = int(input())
print(d[n]%10007)
