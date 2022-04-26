# 전쟁은 어느덧 전면전이 시작되었다. 결국 전투는 난전이 되었고, 우리 병사와 적국 병사가 섞여 싸우게 되었다.
# 그러나 당신의 병사들은 흰색 옷을 입고, 적국의 병사들은 파란색 옷을 입었기 때문에 서로가 적인지 아군인지는 구분할 수 있다.
# 문제는 같은 팀의 병사들은 모이면 모일수록 강해진다는 사실이다.
#
# N명이 뭉쳐있을 때는 N2의 위력을 낼 수 있다. 과연 지금 난전의 상황에서는 누가 승리할 것인가? 단, 같은 팀의 병사들이 대각선으로만 인접한 경우는 뭉쳐 있다고 보지 않는다.
#
# 입력
# 첫째 줄에는 전쟁터의 가로 크기 N, 세로 크기 M(1 ≤ N, M ≤ 100)이 주어진다. 그 다음 두 번째 줄에서 M+1번째 줄에는 각각 (X, Y)에 있는 병사들의 옷색이 띄어쓰기 없이 주어진다.
# 모든 자리에는 병사가 한 명 있다. B는 파란색, W는 흰색이다. 당신의 병사와 적국의 병사는 한 명 이상 존재한다.
#
# 출력
# 첫 번째 줄에 당신의 병사의 위력의 합과 적국의 병사의 위력의 합을 출력한다.
#
# 예제 입력 1
# 5 5
# WBWWW
# WWWWW
# BBBBB
# BBBWW
# WWWWW
# 예제 출력 1
# 130 65

# dfs -> run time error
# our_team = 0
# not_our_team=0
# our_team_result =0
# not_our_team_result =0
# def dfs_w(i,j):
#
#    if i<0 or j<0 or i>=n or j>=m:
#        return False
#
#    if graph[i][j] =='W':
#        graph[i][j] = '1'
#        global our_team
#        our_team+=1
#        dfs_w(i-1,j)
#        dfs_w(i+1,j)
#        dfs_w(i,j-1)
#        dfs_w(i,j+1)
#        return True
#    return False
#
#
# def dfs_b(i, j):
#     if i < 0 or j < 0 or i >= n or j >= m:
#         return False
#
#     if graph[i][j] == 'B':
#         graph[i][j] = '1'
#         global not_our_team
#         not_our_team += 1
#         dfs_b(i - 1, j)
#         dfs_b(i + 1, j)
#         dfs_b(i, j - 1)
#         dfs_b(i, j + 1)
#         return True
#     return False
#
#
#
# n,m=map(int,input().split())
# graph=[]
# for i in range(n):
#     graph.append(list(input()))
#
# for i in range(n):
#     for j in range(m):
#         if dfs_w(i,j) == True:
#             our_team_result+=our_team**2
#             our_team=0
#
# for i in range(n):
#     for j in range(m):
#         if dfs_b(i,j) == True:
#             not_our_team_result += not_our_team ** 2
#             not_our_team = 0
#
# print(our_team_result,not_our_team_result)

# bfs


def bfs(x,y,team):
    queue = deque()
    queue.append((x,y))
    total = 1
    graph[x][y] =1
    while queue:

        x,y =queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny= y+dy[i]
            if nx <0 or ny<0 or nx >= m or ny >= n:
                continue
            if team == graph[nx][ny] :
                total+=1
                queue.append((nx,ny))
                graph[nx][ny]=1


    return total


from collections import deque
n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(input()))

W=0
B=0

dx=[1,-1,0,0]
dy=[0,0,1,-1]

for i in range(n):
    for j in range(m):
        if graph[i][j] !=1:
            if graph[i][j]=='W':
                W += bfs(i,j,'W')**2

            else:
                B += bfs(i,j,'B')**2


print(W,B)



