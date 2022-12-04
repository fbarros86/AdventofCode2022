with open("input.txt","r") as f:
    count=0
    for line in f.readlines():
        pairs = line.split(",")
        fstpair = pairs[0].split("-")
        sndpair = pairs[1].split("-")
        if (int(fstpair[0])>=int(sndpair[0]) and int(fstpair[1])<=int(sndpair[1])):
            count+=1
        elif (int(fstpair[0])<=int(sndpair[0]) and int(fstpair[1])>=int(sndpair[1])):
            count+=1
    print(count)
        