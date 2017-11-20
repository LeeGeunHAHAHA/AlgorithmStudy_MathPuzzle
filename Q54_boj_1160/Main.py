a,b,c,d,e=[ int(input()) for i in range (5)]
ta = b//d+1 if b%d else b//d
tb = c//e+1 if c%e else c//e
ans = a - max(ta,tb)
print(ans if ans >0 else 0)

