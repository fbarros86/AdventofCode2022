with open("input.txt","r") as f:
    elfs=list()
    acc = 0
    for line in f.readlines():
        if (line[0]=="\n"):
            elfs.append(acc)
            acc=0
        else: acc+=int(line)
    elfs.append(acc)
    top1 = max(elfs)
    elfs.remove(top1)
    top2 = max(elfs)
    elfs.remove(top2)
    top3 = max(elfs)
    elfs.remove(top3)
    
    print(top1+top2+top3)