line = [int(i) for i in input().split()]
a = set([input() for i in range(line[0])])
b = set([input() for i in range(line[1])])
c = list(a.intersection(b))
c.sort()
print(len(c))
for i in c:
    print(i)

