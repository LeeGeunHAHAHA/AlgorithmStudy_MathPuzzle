n = int(input())
cards = set(int(i) for i in input().split())
"""dictionary
d =dict()
for i in cards :
d.setdefault(i,True)
"""
t = int(input())
targets = [int(i) for i in input().split()]
for i in targets:
    print(1 if i in cards else 0, end = " " )
