with open("input.txt","r") as f:
    count=0
    for line in f.readlines():
        pairs = line.split(",")
        fstpair = pairs[0].split("-")
        sndpair = pairs[1].split("-")
        fstlist = list(range(int(fstpair[0]),int(fstpair[1])+1))
        sndlist = list(range(int(sndpair[0]),int(sndpair[1])+1))
        if (fstlist[0]>sndlist[0]):
            if (fstlist[0]-sndlist[0] < len(sndlist)): count+=1
        elif (fstlist[0]<sndlist[0]):
            if (sndlist[0]-fstlist[0] < len(fstlist)): count+=1
        else: count+=1
    print(count)
        