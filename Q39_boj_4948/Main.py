from math import sqrt
def cal(n):
    nums = [i for i in range(n+1,2*n+1)]
    print(nums)
    for i in range(2,n+1):
        j =2
        while (2*n//j)+1>=j :
            try :
                nums.remove(i*j) 
            except :
                j+=1
                continue
            j+=1
    print(nums)
    return nums.__len__()

i = int(input())
def sieve(n):
    if n < 2:
        return []
    s = [0, 0] + [1] * (n - 1)
    for i in range(2, int(n**.5)+1):
        if s[i]:
            s[i*2::i] = [0] * ((n - i)//i)
    return [i for i, v in enumerate(s) if v]



def isPrime(t):
    for i in range (2,int(sqrt(t))+1):
        if t%i== 0: return False
    return True

while (i):
    print(len(sieve(2*i))-len(sieve(i)))
    i= int(input())
