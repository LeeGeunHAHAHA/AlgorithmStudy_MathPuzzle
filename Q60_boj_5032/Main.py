h,g,c = [int(i) for i in input().split()]
t = h+g
s =0
while t//c  :
    d = t//c
    m = t%c
    s +=d
    t = d + m
print(s)
