n  = int(input())
a = [ int(i) for i in input().split(" ")]
d = [1 for i in range (n)]
m = 0

def calc(index):
    if d[index] >1 :return d[index]
    if index == n-1:
        return d[index]
    m = d[index]
    for i in range (index,n) :
        if a[index] > a[i] and d[index] + calc(i) > m :
            m = d[index] + calc(i)
    d[index] = m
    return d[index]
for i in range (n-1,-1,-1):
        calc(i)
print(max(d))
    



