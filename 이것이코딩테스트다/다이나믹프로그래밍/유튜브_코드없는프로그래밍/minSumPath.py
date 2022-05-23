# 문제: 2d array로 길을 가기 위한 비용이 주어진다. 왼쪽 위에서 오른족 아래까지 도달하기 위한 최소 비용은 얼마인가?
#f(x,y) = cost(x,y) + min(f(x-1,y), f(x,y-1))


def minimumPath(grid):
    row = len(grid)
    col =  len(grid[0])
    minimum = [[0]*col for i in range (row)]

    # [[1, 4, 5, 7], [3, 0, 0, 0], [6, 0, 0, 0], [7, 0, 0, 0]] 로 초기값 세팅
    minimum[0][0] = grid[0][0]
    for i in range(1,row):
        minimum[0][i] = grid[0][i] + minimum[0][i-1]
    for i in range(1,col):
        minimum[i][0] = grid[i][0] + minimum[i-1][0]

    for i in range(1,row):
        for j in range(1,col):
            minimum[i][j]= grid[i][j]+min(minimum[i-1][j],minimum[i][j-1])

    return minimum[row-1][col-1]

grid = [[1,3,1,2],[2,4,5,2],[3,4,5,6],[1,5,6,2]]
print(minimumPath(grid))