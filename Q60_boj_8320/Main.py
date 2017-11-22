from math import sqrt
n = int(input())
d =[0 for i in range(0,n+1)]
for i in range(len(d)):
    s = 0
    if d[i] :
        s+=i
        if not d[i]  :
            print(i,j,i%j)
            for j in range(0,int(sqrt(i)+1)):
                if i%j : s+=1
            d[i]=s

print(d)
print(s)

