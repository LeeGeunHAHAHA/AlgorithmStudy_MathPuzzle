import math
n = int(input())
r = int(math.sqrt(n))
for i in range(2,r+1):
    if not n%i :
        print(n-(n//i)) 
        break;
    if i == r : print (n-1)
