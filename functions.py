#### PLATEAU ### 1 A B C
def read_grid (path):
    with open(path, "r") as f :
    lignes= f.readlines()
    grid = []
    for ligne in lignes:
        L=[]
        for i in ligne:
            if i == '0'  or i == '1' or i == '2':
                L.append(int(i))
        grid.append(L)
    f.close()


def save_grid(path,grid):
    with open(path, "w") as f :
    for lignes in grid:
        for elem in lignes:
            f.write(str(elem)+ ' ')
        f.write('\n')


def print_grid(grid):
    for row in grid:
        for elem in row:
            if elem==0:
                print(chr(46),end=" ")
            elif elem==1:
                print(chr(35),end=" ")
            else:
                print(chr(35),end=" ")
    print()

    
    
##########3 a
def valid_position(grid,bloc,i,j):
    verif=0
    for l in range(i,i+5):
        for c in range(j,j+5):
            for L in range(len(bloc)):
                for C in range(len(bloc[i])):
                    if grid[l][c]==0 and bloc[L][C]==1:
                        verif=1
                    elif grid[l][c]==1 and (bloc[L][C]==1 or bloc[L][C]==2):
                        verif=1
                    elif grid[l][c]==2 and bloc[L][C]==1:
                        verif=1
    return (bool(verif))

##3 b
def emplace_bloc(grid,bloc,i,j):
    if valid_postion(grid,bloc,i,j)==True:
        for l in range(i,i+5):
            for c in range(j,j+5):
                for L in range(len(bloc)):
                    for C in range(len(bloc[L])):
                        if grid[l][c]==1 and bloc[L][C]==2:
                            grid[l][c]=2
    return grid
  
  
  
  
  
  
###4 a
def row_state(grid,i):
    v=False
    if not(1) in grid[i]:
        v=True
    return v
##4 b
def col_state(grid,j):
    v=0
    for a in range(len(grid)):
        if grid[a][j]=1:
            v=1
    if v=1:
        v=False
    else:
        v=True
    return v
##4 c
def row_clear(grid,i):
    for e in range(i)
        for L in range(len(grid[i])): 
            if grid[i-1][L]==1:
                grid[i][L]=1
            elif grid[i-1][L]==2:
                grid[i][L]=2
        i+=1

##4 d
def col_clear(grid,j):
    for a in range(len(grid)):
        if grid[a][j]!=0:
            grid[a][j]=1
    return grid