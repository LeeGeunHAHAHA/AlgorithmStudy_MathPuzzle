n = int(input())
car = int(input())
ans = []
for i in range(n):
    plus , minus = [int(i) for i in input().split()]
    car = (car + plus - minus)
    ans.append(car)
    if ans[-1] < 0:
        ans = [0]
        break
print(max(ans))
