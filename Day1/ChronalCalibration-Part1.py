#There are ways to condense this
final = 0
data = open("input.txt","r")

for line in data:
    final += int(line)
print(final)
