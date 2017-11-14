d=[1]
d.append(1)
for i in range (2,14):
    d.append(d[i-1]*(i))
print(d[int(input())])
