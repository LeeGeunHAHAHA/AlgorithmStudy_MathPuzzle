import random
import copy
def iSort(target, i):
    if i ==len(target)-1: return
    else :
        for index in range(0,i+1):
            if (target[index]< target[i+1]): target[index], target[i+1] = target[i+1], target[index]
    return iSort(target , i+1)
def sSort(target):
    for i in target :
        for j in range (i+1 , len(target)-i):
            if(target[i]>target[j]): target[i] , target[j] = target[j], target[i]

if __name__ == "__main__" :
    a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,16]
    random.shuffle(a)
    b =copy.deepcopy(a)
    c =copy.deepcopy(a)
    print(a)
    iSort(a,0)
    print(a)
    print(b)
    b.sort(reverse=True)
    print(b)
    print(c)
    sSort(c)
    print(c)


