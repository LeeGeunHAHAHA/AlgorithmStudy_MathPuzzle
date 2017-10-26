d =[[0 for i in range(11)]for i in range(101)]
def process():
    for i in range(10):
        d[1][i] = 1
    d[1][0] =0; d[1][10]=0
    for i in range (2,101):
        for j in range (11) :
            if (j==10) : d[i][j] = 0
            elif j==0 : d[i][j] = d[i-1][1]
            else : d[i][j] = d[i-1][j-1]+d[i-1][j+1]
if __name__=="__main__" :
    n = int(input())
    process()

    answer = sum(d[n])%1000000000
    print(answer)
