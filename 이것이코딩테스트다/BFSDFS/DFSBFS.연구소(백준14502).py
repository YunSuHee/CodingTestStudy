# 인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고,
# 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.
#
# 연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다.
# 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.
#
# 일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다.
# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
#
# 예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.
#
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0
# 이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.
#
# 2행 1열, 1행 2열, 4행 6열에 벽을 세운다면 지도의 모양은 아래와 같아지게 된다.
#
# 2 1 0 0 1 1 0
# 1 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 1 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0
# 바이러스가 퍼진 뒤의 모습은 아래와 같아진다.
#
# 2 1 0 0 1 1 2
# 1 0 1 0 1 2 2
# 0 1 1 0 1 2 2
# 0 1 0 0 0 1 2
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0
# 벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 위의 지도에서 안전 영역의 크기는 27이다.
#
# 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
#
# 둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
#
# 빈 칸의 개수는 3개 이상이다.
#
# 출력
# 첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.
#
# 예제 입력 1
# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0
# 예제 출력 1
# 27
# 예제 입력 2
# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2
# 예제 출력 2
# 9
# 예제 입력 3
# 8 8
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 예제 출력 3
# 3

import itertools
import copy
from collections import deque
n, m = map(int,input().split())

graph =[]
for i in range(n):
    graph.append(list(map(int,input().split())))

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

#0 빈칸 위치 담기
#2 바이러스 위치 담기
blank = []
birus = []
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            blank.append(str(i)+' '+str(j))
        if graph[i][j]==2:
            birus.append(str(i) + ' ' + str(j))

# 조합으로 벽 위치 3군데 찾기
wall = itertools.combinations(blank,3)
wall_list =list(wall)


#wall 위치 지정해서
def wall(wall,graph):

    temp_graph = copy.deepcopy(graph)
    for i in wall:
        x,y=map(int,i.split())
        temp_graph[x][y] = 1

    return bfs(temp_graph)

#0 카운트 하는 bfs
def bfs(graph):
    queue = deque()
    total =0
    for i in birus:
        x, y = map(int, i.split())
        queue.append((x,y))

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx <0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny] == 0:
                queue.append((nx,ny))
                graph[nx][ny] = 2
            else:
                continue
    for i in graph:
        total+= i.count(0)
    return total

# 최대값 찾기
result = 0

for i in wall_list:
    temp=wall(i,graph)
    if result < temp:
        result = temp
print(result)

###################################################################################################


### 이코테 정답
n, m = map(int, input().split())
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트
graph = [list(map(int, input().split())) for _ in range(n)] # 초기 맵 리스트

result = 0

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 깊이 우선 탐색을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상,하,좌,우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스를 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최댓값 계산
        result = max(result, get_score())
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1

dfs(0)
print(result)
