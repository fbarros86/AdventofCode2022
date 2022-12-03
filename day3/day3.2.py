with open("input.txt","r") as f:
    rucksacks = list()
    counter=0
    aux = list()
    for line in f.readlines():
        l = line[:-1]
        if (counter==3):
            rucksacks.append(aux)
            counter=0
            aux=list()
        aux.append(l)
        counter+=1
    rucksacks.append(aux)
    sum=0
    for [r1,r2,r3] in rucksacks:
        common = set()  
        for c in r1:
            if c not in common and c in r2 and c in r3:
                common.add(c)
                if (c>="a" and c<="z"):sum+= ord(c)-ord("a")+1
                elif (c>="A" and c<="Z"):sum+= ord(c)-ord("A")+27
    print(sum)