import sys
maps =  set()

def cal():
    line  = [ int(i) for i in sys.stdin.readline().strip().split()]
    r = line[0] 
    c = line[1]-1 
    start = c *100 + r -101
    for i in range (10):
        start += 100
        for j in range (start , start+10) :
            maps.add(j)
            

    
t = int(sys.stdin.readline().strip())
while t :
    cal()
    t-=1
print(len(maps))
    
