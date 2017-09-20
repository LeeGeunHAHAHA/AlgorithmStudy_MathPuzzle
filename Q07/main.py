d = []
n =int(input())
data= input().split()
for i in range(0,n) :
    data[i] = int(data[i])
    d.append(0)
def dp() :
    global d, data
    d[0] = data[0]
    for i in range(1,len(data)):
        if(d[i-1]>=0) :
            d[i] = d[i-1] +data[i]
        else : d[i] = data[i]
    d.sort()
    print(d.pop())
if __name__=="__main__" : 
    dp()
