lenofseq = int(input())
sumseq = [(i+1)*int(s) for i, s in enumerate(input().split())]
ans = list()
for i,j in enumerate(sumseq):
    a = j
    if i:
        a = j-sumseq[i-1]
    ans.append(a)
    print(a, end =" ")
