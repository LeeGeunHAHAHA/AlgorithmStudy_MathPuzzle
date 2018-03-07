seat = int(input())
seat_code = input()
couple = seat_code.count("LL")
print(seat - couple +1 if couple else seat  ) 
