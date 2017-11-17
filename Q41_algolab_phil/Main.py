from copy import deepcopy
from math import log
class p :
    x =0
    y =0
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def show(self) :
        print(self.x,self.y)
    def yx(self):
        self.x, self.y = self.y, self.x
        return self
    def rev(self):
        self.x , self.y = -self.y, -self.x
        return self
    def move(self, dx,dy):
        self.x+=dx
        self.y+=dy
        return self
    def __str__(self):
        return "0"

def makeNext(target, m):
    tmp=[]
    res =[]
    for i in range (4):
        tmp.append(deepcopy(target))
    for i in tmp[0] :
        res.append(i.yx())
    for i in tmp[1] :
        res.append(i.move(0,m))
    for i in tmp[2] :
        res.append(i.move(m,m))
    for i in tmp[3] :
        res.append(i.rev().move(m+1+m,m+1))
    return res
s = [p(1,1), p(1,2),p(2,2),p(2,1)]
maps =[]
maps.append(s)
test = makeNext(maps[0],2)
test2 = makeNext(test,4)
test[9].show()
test2[18].show()
for i in range (2,8):
    maps.append(makeNext(maps[-1],int(pow(2,i-1))))
inputs = [int(i) for i in input().split()]
x = int(log(inputs[0],2))-1
y = inputs[1]-1 
print(len(maps))
maps[x][y].show()
