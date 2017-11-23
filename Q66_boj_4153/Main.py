while 1 :
    a,b,c = sorted(map(int,input().split()))
    if (not a) and (not b) and (not c) : break
    ans = "right" if c**2 == a**2 + b**2 else "wrong"
    print(ans)
