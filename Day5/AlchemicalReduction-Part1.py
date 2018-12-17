#really need to revisit, couldve been done easier and neater
data = open("AlchemicInput.txt","r").read().split()
h = ['q']
for i in data:
    for j in i:
        if j.lower() != h[-1].lower() or j == h[-1]:
            h.append(j)
        else:
            h.pop(-1)
        

print(len(''.join(h))-1)
