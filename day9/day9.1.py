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
    hpos = (0,0)
    tpos = (0,0)
    vis = {(0,0)}
    for line in f.readlines():
        words = line.split()
        direction = words[0]
        number = words[1]
        for i in range(int(number)):
            hpos = move(direction,hpos)
            tpos = newTail(tpos,hpos)
            vis.add(tpos)
    print(len(vis))