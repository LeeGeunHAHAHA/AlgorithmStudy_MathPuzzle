#!/usr/bin/env python3
testCase = 3
while testCase:
    work_time = list(map(int,input().split()))
    def toSec():
        work_time[2] += 60*(60*work_time[0]+work_time[1])
        work_time[5] += 60*(60*work_time[3]+work_time[4])
        return work_time[5]-work_time[2]
    ans = toSec()
    s = ans%60
    ans //=60
    m = ans%60
    h = ans//60
    print(h,m,s)
    testCase-=1


