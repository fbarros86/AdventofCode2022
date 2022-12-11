with open("input.txt", "r") as f:
    currentCycle = 0
    x = 1
    mapa = ""
    for line in f.readlines():
        if (currentCycle>241): break
        elif (line[0]=="n"):
            pos = currentCycle%40
            if(pos==0):mapa+="\n"
            if (pos==x or pos==x-1 or pos==x+1): mapa+="#"
            else: mapa+="."
            currentCycle+=1
        else:
            numberToAdd = line.split()[1]
            pos = currentCycle%40
            if(pos==0):mapa+="\n"
            if (pos==x or pos==x-1 or pos==x+1): mapa+="#"
            else: mapa+="."
            currentCycle+=1
            pos = currentCycle%40
            if(pos==0):mapa+="\n"
            if (pos==x or pos==x-1 or pos==x+1): mapa+="#"
            else: mapa+="."
            currentCycle+=1
            x+=int(numberToAdd)
    print(mapa)
        
