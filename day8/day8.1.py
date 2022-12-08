def up(x,y,m):
    value  = m[x][y]
    for i in range(0,x):
        if m[i][y]>= value: return False
    return True

def down(x,y,m):
    value  = m[x][y]
    for i in range(x+1,len(m)):
        if m[i][y]>= value: return False
    return True

def left(x,y,m):
    value  = m[x][y]
    for j in range(0,y):
        if m[x][j]>= value: return False
    return True

def right(x,y,m):
    value  = m[x][y]
    for j in range(y+1,len(m[0])):
        if m[x][j]>= value: return False
    return True

with open("input.txt", "r") as f:
    matrix = list()
    for line in f.readlines():
        l = list()
        for column in line:
            l.append(ord(column))
        matrix.append(l[:-1])
count = 0
count += len(matrix) * 2
count += (len(matrix[0]) - 2) * 2
for i in range(1, len(matrix) - 1):
    for j in range(1, len(matrix[0]) - 1):
        if (up(i,j,matrix) or down(i,j,matrix) or left(i,j,matrix) or right(i,j,matrix)):
            count += 1
print(count)
