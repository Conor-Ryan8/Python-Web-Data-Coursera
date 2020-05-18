import re
Filename = input('Input Filename: ')
Handle = open(Filename)
Sum = 0
Count = 0
for Line in Handle:
  Line = Line.rstrip()
  List = re.findall('[0-9]+',Line)
  for Value in List:
    Sum = Sum + int(Value)
    Count = Count+1
print(Count,'Values, with a Sum of:',Sum)
