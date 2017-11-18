t = int(input())
while t :
    tmp = [int(i) for i in input().split()]
    ans = ["advertise","does not matter", "do not advertise"]
    y = tmp[0]
    n = tmp[-2]-tmp[-1]
    if y < n: print(ans[0])
    elif y == n : print(ans[1])
    else : print(ans[2])
    t-=1
