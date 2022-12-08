class Directory:
    def __init__(self,path):
        self.path = path
        self.dirs = list()
        self.fsize = 0
        self.files = set()
        self.sizeDirs = None
        
    def __eq__(self,other):
        return self.path==other.path

    
def calculateDirSize(d:Directory,directories):
    d.sizeDirs=0
    for dir in d.dirs:
        d.sizeDirs+=directories[getPath(dir)].fsize
        if (not directories[getPath(dir)].sizeDirs):calculateDirSize(directories[getPath(dir)],directories)
        d.sizeDirs+=directories[getPath(dir)].sizeDirs
        
def getPath(pathlist):
    s=""
    for p in pathlist:
        s+=p
    return s

with open("input.txt","r") as f:
    currentDir = Directory(["/"])
    directories={"/":currentDir}
    i=0
    for line in f.readlines():
        i+=1
        if (line=="$ cd /\n"):pass
        else:
            word=line.split()
            if (line[0]=="$" and word[1]=="cd" and word[2]!=".."):
                newpath = currentDir.path + [word[2]]
                if (newpath not in currentDir.dirs):currentDir.dirs.append(newpath)
                if (getPath(newpath) not in directories):
                    directories[getPath(newpath)] = Directory(newpath)
                currentDir = directories[getPath(newpath)]
            elif (line[0]=="$" and word[1]=="cd" and word[2]==".."):
                currentDir = directories[getPath(currentDir.path[:-1])]
            elif (line[0]!="$" and word[0]=="dir"):
                if ((currentDir.path + [word[1]]) not in currentDir.dirs):
                    currentDir.dirs.append(currentDir.path + [word[1]])
            elif (line[0]!="$"):
                if (word[1] not in currentDir.files):
                    currentDir.fsize+=int(word[0])
                    currentDir.files.add(word[1])
    for dir in directories.values():
        if (not dir.sizeDirs): calculateDirSize(dir,directories)
    sum=0
    for dir in directories.values():
        if (dir.fsize+dir.sizeDirs <= 100000):
            sum+=dir.fsize+dir.sizeDirs 
    print(sum)
    