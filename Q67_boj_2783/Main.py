from functools import reduce
a = reduce(lambda x, y: int(x)/int(y)*1000,input().split())
n = int(input())
ans=min( [reduce(lambda x,y: int(x)/int(y)*1000,input().split()) for i in range(n)])
fin = ans if ans<a else a
print(round(fin,2))

