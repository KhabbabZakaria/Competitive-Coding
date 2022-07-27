#example:
'''
input:
matrix = [
  [1, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 1, 1],
  [0, 0, 1, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 1, 1, 0, 0],
  [1, 0, 0, 0, 0, 1]
]

output:
matrix = [
  [1, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 1],
  [0, 0, 0, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 1]
]
'''
def removeIslands(matrix):
    # Write your code here.
    lands = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
    visited = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for j in range(len(matrix[0])):
        if matrix[0][j]==1:
            lands[0][j] = True
            visited[0][j] = True
            lands = dfs(matrix, 0, j, lands, visited)
            
    for j in range(len(matrix[-1])):
        if matrix[len(matrix)-1][j]==1:
            lands[len(matrix)-1][j] = True
            visited[len(matrix)-1][j] = True
            lands = dfs(matrix, len(matrix)-1, j, lands, visited)
            
    for i in range(len(matrix)):
        if matrix[i][0]==1:
            lands[i][0]=True
            visited[i][0]=True
            lands = dfs(matrix, i, 0, lands, visited)
            
    for i in range(len(matrix)):
        if matrix[i][len(matrix[0])-1]==1:
            lands[i][len(matrix[0])-1]=True
            visited[i][len(matrix[0])-1]=True
            lands = dfs(matrix, i, len(matrix[0])-1, lands, visited)
            
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if lands[i][j]==False:
                matrix[i][j]=0
    return matrix

def getneighbors(matrix, i, j):
    neighbors = []
    if i>=1:
        neighbors.append([i-1,j])
    if i<=len(matrix)-2:
        neighbors.append([i+1,j])
    if j>=1:
        neighbors.append([i,j-1])
    if j<=len(matrix[0])-2:
        neighbors.append([i,j+1])
    return neighbors

def dfs(matrix, i, j, lands, visited):
    possibilities = []
    neighbors = getneighbors(matrix, i, j)
    possibilities.extend(neighbors)
    while len(possibilities):
        r,c = possibilities.pop()
        if matrix[r][c]==1:
            lands[r][c]=True
            visited[r][c]=True
            neighbors2 = getneighbors(matrix, r, c)
            neighbors3 = neighbors2[:]
            for [r2,c2] in neighbors2:
                if visited[r2][c2]:
                    neighbors3.remove([r2,c2])
            neighbors2 = neighbors3
            possibilities.extend(neighbors2)
    return lands
