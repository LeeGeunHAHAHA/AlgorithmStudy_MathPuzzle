testCase = int(input())
def cal():
    """
    print "OK" when data is OK
    else "FAKE"
    """
    chdic =dict()
    line = input()
    for chr in line :
        if chr not in chdic:
            chdic.setdefault(chr,1)
        else:
            chdic[chr] += 1
        chdic[chr]
    print(chdic)

while testCase :
    cal()
    testCase -= 1
