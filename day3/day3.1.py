with open("input.txt","r") as f:
    rucksacks = list()
    for line in f.readlines():
        halflen = int((len(line)-1)/2)
        rucksacks.append((line[:halflen],line[halflen:-1]))
    sum=0
    for r1,r2 in rucksacks:  
        common = set()
        for c in r1:
            if c in r2 and c not in common:
                common.add(c)
                if (c>="a" and c<="z"):sum+= ord(c)-ord("a")+1
                elif (c>="A" and c<="Z"):sum+= ord(c)-ord("A")+27
    print(sum)
                