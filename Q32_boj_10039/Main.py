a =[]
for i in range(5):
    tmp = int(input())
    a.append(tmp if tmp>40 else 40)
print(sum(a)//5)
