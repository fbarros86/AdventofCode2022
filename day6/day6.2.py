with open("input.txt","r") as f:
    current = list()
    line = f.readline()
    i=0
    for c in line:
        if (len(current)==14):
            print(i)
            break
        if (c in current):
            while (c in current):
                current.pop(0)
            current.append(c)
        else:current.append(c)
        i+=1
            
    