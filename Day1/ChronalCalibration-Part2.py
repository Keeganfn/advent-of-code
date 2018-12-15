#Part 2
#Could make this faster by using itertools and set/dictionary instead of list
final = 0
frequency = []
data = open("input.txt","r")

for line in data:
    final += int(line)
    frequency.append(final)
while True:
    data.seek(0)
    for line in data: 
        final += int(line)
        for i in frequency:
            if i == final:
                print(final)
                quit()