d = dict()
legend = """
1967 DavidBowie
1969 SpaceOddity
1970 TheManWhoSoldTheWorld
1971 HunkyDory
1972 TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars
1973 AladdinSane
1973 PinUps
1974 DiamondDogs
1975 YoungAmericans
1976 StationToStation
1977 Low
1977 Heroes
1979 Lodger
1980 ScaryMonstersAndSuperCreeps
1983 LetsDance
1984 Tonight
1987 NeverLetMeDown
1993 BlackTieWhiteNoise
1995 1.Outside
1997 Earthling
1999 Hours
2002 Heathen
2003 Reality
2013 TheNextDay
2016 BlackStar
"""
line = legend.strip().split('\n')
for i in line :
    tmp = i.split()
    if d.__contains__(int(tmp[0])) :
        #print(tmp[1])
        #print(d[int(tmp[0])])
        d[int(tmp[0])] +=" "+ tmp[1] 
    else : d.update({int(tmp[0]):tmp[1]})
t = int(input())
ans =[]
while t :
    se = [int(i) for i in input().split()]
    for i in range (se[0] , se[1] +1):
        if d.__contains__(i):
            for j in d[i].split():
               ans.append((i,j))
    print(len(ans))
    for i in ans:
        print(i[0],i[1])
    ans.clear()
    t-=1
