num = int(input())
p = list(map(int, input().split()))
p.insert(0,0)
d = [0 for i in range(1001)]
ans =0
for i in range (1,num +1) :
    ans = max([d[i-j] + p[j] for j in range(1, i+1)])
    d[i] = ans
  # for j in range (1,i+1) :
  #     ans.append(d[i-j] +p[j])
  #     d[i] = max(ans)
print(d[num])



        
