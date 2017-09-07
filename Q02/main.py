from random import*
c=x=eval("int(input()),"*9)
while sum(x)!=100:
	x=sample(c,7)
x.sort()
for i in x:
	print(i)
