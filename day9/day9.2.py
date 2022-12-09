def move(direction,hpos):
    x,y= hpos
    if (direction=="U"): return (x,y+1)
    elif (direction=="D"): return (x,y-1)
    elif (direction=="L"): return (x-1,y)
    elif (direction=="R"): return (x+1,y)

def newTail(t,h):
    xt,yt=t
    xh,yh=h
    if (abs(xt-xh)<=1 and abs(yh-yt)<=1): return t
    elif (xt==xh): return (xt,yt+((yh-yt)/(abs(yh-yt))))
    elif (yt==yh): return (xt+((xh-xt)/(abs(xh-xt))),yt)
    else: return(xt+((xh-xt)/(abs(xh-xt))), yt+(yh-yt)/(abs(yh-yt)))
    

with open("input.txt","r") as f:
    posList=list()
    for i in range(10):
        posList.append((0,0))
    vis = {(0,0)}
    for line in f.readlines():
        words = line.split()
        direction = words[0]
        number = words[1]
        for i in range(int(number)):
            posList[0] = move(direction,posList[0])
            for j in range(1,10):
                posList[j] = newTail(posList[j],posList[j-1])
            vis.add(posList[9])
    print(len(vis))