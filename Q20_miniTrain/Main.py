import copy
def getInput():
    n = int(input())
    line = input().split()
    train = [int(i) for i in line]
    lenOfmin = int(input())
    return train , lenOfmin
train , LOM = getInput()
backup = copy.deepcopy(train)
d = {}

def partSum(t,index):
    i = index 
    s= sum(t[i:i+LOM])
    return s
def clean(t,i) :
    t[i:i+LOM] = [0 for i in range(LOM)]

def saveD(indexes, s):
    t = tuple(indexes)
    d.update({t,s})
def findR(f) :
    if flag ==3 :
        s = partSum(train,0)
        for i in range (1,len(train)-LOM):
            tmp = partSum(train,i)
            if tmp > s : s = tmp
        return s
    


                

                
if __name__ == "__main__" :
   print(partSum(train ,0)) 
   print(train)
   print(findMax(train))
