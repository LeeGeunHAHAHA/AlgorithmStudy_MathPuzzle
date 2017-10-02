import math as m
prime = [ i for i in range(2,10000)]
for i in prime:
    for j in range(2,10000//i+1):
            try:
                prime.remove(i*j)
            except:
                continue
def golden():
    pn = int(input())
    for i in range(pn//2,0,-1):
        if prime.count(i) and prime.count(pn-i):
                print(i,pn-i)
                break
if __name__ == "__main__":
    testCase = int(input())
    for i in range(testCase):
        golden()
