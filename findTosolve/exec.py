#!/usr/bin/env python3
import random

def toSolveList():
    with open("toSolve.txt","r")as f:
        a = f.readline()
        toSolve =a.split(",")
        for i in range(0,len(toSolve)):
               toSolve[i] = int(toSolve[i]) 
        return toSolve  
def solvedList():
    with open("solved.txt","r")as f:
        a = f.readline()
        solved =a.split(" ")
        for i in range(0,len(solved)):
               solved[i] = int(solved[i]) 
        return solved
def find():
    toSolve = toSolveList()
    toSolve.sort()
    solve =solvedList()
    solve.sort()
    for i in solve :
        try:
            toSolve.remove(i)
        except:
            continue
    return toSolve
if __name__=="__main__":
    a=find()
    recomend = random.sample(a,3)
    print("Toaday's Recomeded Random Puzzle")
    for i in recomend:
        print("boj.kr/"+str(i))
    with open("recomed.txt","w")as f:
        for i in a:
            f.write(str(i) + "\n")
