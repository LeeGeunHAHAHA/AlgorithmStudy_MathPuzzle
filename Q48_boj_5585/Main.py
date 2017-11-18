t = 1000 - int(input())
print(t)
c = 0
c += t//500 ; t%=500
c += t//100 ; t%=100
c += t//50 ; t%= 50
c += t//10 ; t%= 10
c += t//5 ; t%= 5
c += t//1 ; t%= 1
print(c)
