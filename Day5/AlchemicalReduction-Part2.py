#Really need to revisit, couldve been done easier and neater
import string
data = open("AlchemicInput.txt","r").read().split()

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)

y = []

for g,h in zip(lower,upper):
    for i in data:
        for e in i:
            if e != g and e != h:
                y.append(e)
    r = [str(''.join(y))]
    h = ['q','q']
    for i in r:
        for j in i:
            if j.lower() != h[-1].lower() or j == h[-1]:
                h.append(j)
            else:
                h.pop(-1)
            

    print(len(''.join(h))-2)
    print(g)
    r.clear()
    y.clear()
