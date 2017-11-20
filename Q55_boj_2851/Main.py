mush = [int(input()) for i in range(10)]
score = 0
for i in mush :
    if abs(score-100) < abs(score+i-100) :
        print(i)
        print(score)
        break
    else: score +=i
if score == sum(mush) : print(score)
