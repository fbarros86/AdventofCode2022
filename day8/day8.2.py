def up(x,y,m):
    value  = m[x][y]
    count=0
    aaaa  = list(range(0,x))
    aaaa.reverse()
    for i in aaaa:
        count+=1
        if m[i][y]>= value: return count
    return count

def down(x,y,m):
    value  = m[x][y]
    count=0
    for i in range(x+1,len(m)):
        count+=1
        if m[i][y]>= value: return count
    return count

def left(x,y,m):
    value  = m[x][y]
    count=0
    aaaa  = list(range(0,y))
    aaaa.reverse()
    for j in aaaa:
        count+=1
        if m[x][j]>= value: return count
    return count

def right(x,y,m):
    value  = m[x][y]
    count=0
    for j in range(y+1,len(m[0])):
        count+=1
        if m[x][j]>= value: return count
    return count

with open("input.txt", "r") as f:
    matrix = list()
    for line in f.readlines():
        l = list()
        for column in line:
            l.append(ord(column))
        matrix.append(l[:-1])
max = 0
for i in range(1, len(matrix) - 1):
    for j in range(1, len(matrix[0]) - 1):
        n = up(i,j,matrix)* down(i,j,matrix) *left(i,j,matrix) * right(i,j,matrix)
        if (n>max): max = n
print(max)
