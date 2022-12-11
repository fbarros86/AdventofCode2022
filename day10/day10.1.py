with open("input.txt", "r") as f:
    currentCycle = 0
    x = 1
    r=0
    for line in f.readlines():
        if (currentCycle>221): break
        elif (line[0]=="n"):
            currentCycle+=1
            if ((currentCycle+20)%40 == 0):
                r+=currentCycle*x
                print(currentCycle,x)
        else:
            numberToAdd = line.split()[1]
            currentCycle+=1
            if ((currentCycle+20)%40 == 0):
                r+=currentCycle*x
                print(currentCycle,x)

            currentCycle+=1
            if ((currentCycle+20)%40 == 0):
                r+=currentCycle*x
                print(currentCycle,x)
            x+=int(numberToAdd)
    print(r)
        
