n = int(input())
An = sorted(map(int, input().split()))
m = int(input())
Qn = list(map(int, input().split()))
dic = dict()
for i in An:
    dic.setdefault(i)
for i in Qn :
    if dic.__contains__(i):
        print(1)
    else :
        print(0)
