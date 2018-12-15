#Not very pretty, could improve neatness and efficiency 
data = open("InventoryInput.txt","r")
split = []
three = 0
two = 0

for line in data:
    threeCheck = 0
    twoCheck = 0
    for i in line:
        split.append(i)
    d = {x:split.count(x) for x in split}
    for j in d:
        if d[j] == 3 and threeCheck == 0:
            threeCheck+=1
            three+=1
        if d[j] == 2 and twoCheck == 0:             
            twoCheck+=1
            two+=1
    d.clear()
    split.clear()
total = three * two
print(total)
