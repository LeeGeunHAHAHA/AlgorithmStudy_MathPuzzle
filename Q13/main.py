def func(a):
    if a<0:return -a
    else : return a
t = int(input())
for v in range(0,t):
    line = input()
    tmp = line.split()
    n = int(tmp[0])
    k = int(tmp[1])
    nums = []
    sums = []
    line = input()
    tmp2 = line.split()
    for g in tmp2:
        nums.append(int(g))
    for i in range(0,n):
        for j in range(i+1,n):
            sums.append(nums[i]+nums[j]-k)
    sums.sort(key=func)
    cnt = 1
    for i in range(0,len(sums)):
        if sums[i]==sums[i+1] or sums[i]==-sums[i+1]: cnt+=1
        else : break
    print (cnt)
