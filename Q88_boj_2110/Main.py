


n , ap = map(int, input().split())
house = sorted([int(input()) for i in range(n)])
left =1
right = house[-1]
cnt =int()
ans =int()
while (left<= right or cnt <ap):
   cnt = 1
   mid = (left+right)//2
   start = house[0]
   for i in range(1,len(house)):
       if  house[i] - start >= mid:
           cnt+=1
           start = house[i]
   if cnt >= ap :
       ans = mid
       left = mid+1
   else :
       right = mid-1
print(ans)
