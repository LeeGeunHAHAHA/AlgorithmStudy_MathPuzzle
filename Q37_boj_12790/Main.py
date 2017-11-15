p = int(input())

while p  :
    data = [int(i) for i in input().split()]
    stat = [data[i]+data[i+4] for i in range(4)]
    cal = (stat[0] if stat[0] >0 else 1) + (5*stat[1] if stat[1] >0 else 5) +  (stat[2]*2 if stat[2] >0 else 0) + stat[3]*2
    print(cal)
    p-=1
