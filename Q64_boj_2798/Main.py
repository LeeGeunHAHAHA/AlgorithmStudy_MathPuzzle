import bisect
c, ub = map(int, input().split())
cards = list(map(int, input().split()))
sums =[]
for i in range(len(cards)-2):
    for j in range(i+1,(len(cards)-1)):
            for k in range(j+1,(len(cards))):
                sums.append(cards[i]+cards[j]+cards[k])
t=sorted(sums)
idx=bisect.bisect(t,ub)
print(t[idx-1])
    
    
