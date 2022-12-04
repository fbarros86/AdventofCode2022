with open("input.txt","r") as f:
    elfs=list()
    acc = 0
    for line in f.readlines():
        if (line[0]=="\n"):
            elfs.append(acc)
            acc=0
        else: acc+=int(line)
    elfs.append(acc)
    print(max(elfs))