n = input()
k = float(n)
nt= list(n)
if k > 10:
    nt =list(str(int(k)))
    if int(nt[1]) >=5:
        nt[0]=str(int(nt[0])+1)
    nt[1:] = ["0"] * (len(nt)-1)
if k<10 and nt[2]!="0" and len(nt)>1 :
    if int(nt[2]) >= 5:
        nt[0]=str(int(nt[0])+1)
    nt[1:] = []
    nt[1:] = ["0"] * (len(nt)-1)

for j in range(2, len(nt)-1) :
    if nt[j+1] != 0 :
        if int(nt[j+1]) >= 5:
            nt[j]=str(int(nt[j])+1)
            nt[j+1:] = []
            break


print("".join(nt))
