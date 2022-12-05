with open("input.txt","r") as f:
    stacks=list()
    for line in f.readlines():
        if line[0]!="m" and line[0]!="\n":
            i=0
            lenline = len(line)
            while (i<lenline):
                if (len(stacks)<((i/4)+1)): stacks.append(list())
                if (line[i]=="["): stacks[int(i/4)].insert(0,line[i+1])
                i+=4
        elif line[0]=="m":
            words = line.split()
            numberToMove = int(words[1])
            sFrom = int(words[3])
            sTo = int(words[5])
            for _ in range(numberToMove):
                elem = stacks[sFrom-1].pop()
                stacks[sTo-1].append(elem)
    r = ""
    for s in stacks:
        r+=s.pop()
    print(r)
