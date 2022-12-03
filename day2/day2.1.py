def convert(cena):
    if (cena=="A"): return "X"
    elif (cena=="B"): return "Y"
    elif (cena=="C"): return "Z"

with open("input.txt","r") as f:
    points=0
    for line in f.readlines():
        opponent = convert(line[0])
        me = line[2]
        if (me=="X"): points+=1
        elif (me=="Y"): points+=2
        elif (me=="Z"): points+=3
        if (opponent==me): points+=3
        elif (me=="X" and opponent=="Z"): points+=6
        elif (me=="Y" and opponent=="X"): points+=6
        elif (me=="Z" and opponent=="Y"): points+=6
    print(points)
        