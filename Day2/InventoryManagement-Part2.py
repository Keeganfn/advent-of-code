#it works but this is an abomination, need to revisit and try to improve neatness and efficiency
data = open("InventoryInput.txt","r")
inventories = data.readlines()
lineOne = []
lineTwo = []
x=0
while True:
    for i in range(len(inventories)):
        for line in inventories[x]:
            lineOne.append(line)
        for line in inventories[i]:
            lineTwo.append(line)
        incorrect = 0
        for j in range(len(lineOne)):
            if lineOne[j] != lineTwo[j] and incorrect < 2:
                incorrect+=1
        if incorrect == 1:
            for j in range(len(lineOne)):
                if lineOne[j] != lineTwo[j]:
                    lineOne.pop(j)
                    lineTwo.pop(j)
                    break
            print(*lineOne)
            print(*lineTwo)
            quit()
        
        lineOne.clear()
        lineTwo.clear() 
    x+=1
    

