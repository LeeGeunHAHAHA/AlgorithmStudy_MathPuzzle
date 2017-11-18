inputs = [int(input()) for i in range(5)]
a = min(inputs[0]*inputs[-1] , inputs[1] if inputs[2] > inputs[-1] else inputs[1]+inputs[-2]*(inputs[-1]-inputs[2])) 
print(a)
