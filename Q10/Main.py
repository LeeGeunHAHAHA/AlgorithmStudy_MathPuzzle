
def bruteForce(n):
    a = 0; b=0; c=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                a= i*(i+1)//2
                b= j*(j+1)//2
                c= k*(k+1)//2
                if a+b+c == n: return 1
    return 0


if __name__ == "__main__":
    with open("input.txt",'r') as f:
        testCase = int(f.readline())
        while testCase!=0:
            n= int(f.readline())
            print(bruteForce(n))
            testCase=testCase-1
