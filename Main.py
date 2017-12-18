from itertools import permutations as pm
n = int(input())
nums = [int(i) for i in input().split()]
t = [i for i in range(1,n+1)]
p = pm(t)
if nums[0] == 1:
    ans = tuple()
    for i in range (nums[1]) :
        ans = p.__next__()
    for i in ans :
        print(i,end = " " )
if nums[0] ==2:
    target = tuple(nums[1:])
    i = 1
    while (target!= p.__next__()):
        p.__next__()
        i+=1
    print(i+1)
    


