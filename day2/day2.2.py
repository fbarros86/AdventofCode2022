
with open("input.txt","r") as f:
    points=0
    for line in f.readlines():
        opponent = line[0]
        me = line[2]
        if (me=="X"):
            if (opponent=="A"): points+=3
            elif (opponent=="B"): points+=1
            elif (opponent=="C"): points+=2
        elif (me=="Y"):
            points+=3
            if (opponent=="A"): points+=1
            elif (opponent=="B"): points+=2
            elif (opponent=="C"): points+=3
        elif (me=="Z"):
            points+=6
            if (opponent=="A"): points+=2
            elif (opponent=="B"): points+=3
            elif (opponent=="C"): points+=1
        
    print(points)
        