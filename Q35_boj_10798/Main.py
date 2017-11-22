a =""
strings =[input() for i in range (5)]
print(strings)
i =0
while i<16:
    for j in strings: 
        if len(j)>i:
            a+=j[i]
            
    i+=1
print(a)
