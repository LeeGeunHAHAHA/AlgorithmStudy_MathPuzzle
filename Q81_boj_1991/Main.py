n = int(input())

Alpha = [list(map(lambda x: ord(x) - 65 if x != "." else None , input().split())) for i in range (n)]
Alpha.sort(key = lambda x :x[0])
def preOrd(root) :
    print(chr(root[0]+65),end="")
    if root[1] != None:
        preOrd(Alpha[root[1]])
    if root[2] != None:
        preOrd(Alpha[root[2]])
def inOrd(root) :
    if root[1] != None:
        inOrd(Alpha[root[1]])
    print(chr(root[0]+65),end="")
    if root[2] != None:
        inOrd(Alpha[root[2]])
def postOrd(root) :
    if root[1] != None:
        postOrd(Alpha[root[1]])
    if root[2] != None:
        postOrd(Alpha[root[2]])
    print(chr(root[0]+65),end="")
preOrd(Alpha[0])
print("")
inOrd(Alpha[0])
print("")
postOrd(Alpha[0])
print("")
