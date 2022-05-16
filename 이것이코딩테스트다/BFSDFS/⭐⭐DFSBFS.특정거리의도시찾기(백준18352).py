# 어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.
#
# 이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는
# 프로그램을 작성하시오. 또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.
#
# 예를 들어 N=4, K=2, X=1일 때 다음과 같이 그래프가 구성되어 있다고 가정하자.
#
#
#
# 이 때 1번 도시에서 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 2인 도시는 4번 도시 뿐이다.
# 2번과 3번 도시의 경우, 최단 거리가 1이기 때문에 출력하지 않는다.
#
# 입력
# 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다.
# (2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N) 둘째 줄부터 M개의 줄에 걸쳐서
# 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다. 이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다.
# (1 ≤ A, B ≤ N) 단, A와 B는 서로 다른 자연수이다.
#
# 출력
# X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.
#
# 이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.
#
# 예제 입력 1
# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4
# 예제 출력 1
# 4
# 예제 입력 2
# 4 3 2 1
# 1 2
# 1 3
# 1 4
# 예제 출력 2
# -1
# 예제 입력 3
# 4 4 1 1
# 1 2
# 1 3
# 2 3
# 2 4
# 예제 출력 3
# 2
# 3

#풀이 1 - 메모리 초과
# from collections import deque
# n,m,k,x=map(int,input().split())
# arr=[[0]*(n+1) for i in range(n+1)]
# for i in range(m):
#     a,b = map(int, input().split())
#     arr[a][b]=1
# city=[i for i in range(1,n+1)]
#
# q= deque()
# for i in range(1,n+1):
#     if arr[x][i] ==1:
#         q.append((1,x,i))
#         city.remove(i)
#
#     if x in city:
#         city.remove(x)
# result=[]
# while q:
#
#     d, s, e = q.popleft()
#
#     if d > k: break
#     if d == k: result.append(e)
#     if e in city:
#         city.remove(e)
#
#     for i in range(1, n + 1):
#         if arr[e][i] == 1 and i in city:
#             q.append((d + 1, e, i))
#
# if len(result)==0:
#     print(-1)
# else:
#     for i in result:
#         print(i)

#풀이 2 - 시간 초과
# from collections import deque
# n,m,k,x=map(int,input().split())
# node = [list(map(int,input().split())) for i in range(m)]
# city=[i for i in range(1,n+1)]
#
# q=deque()
# for i in node:
#     if i[0]== x:
#         q.append([1,i[0],i[1]])
#         city.remove(i[1])
#
# city.remove(x)
#
# result=[]
# while q:
#     t=q.popleft()
#     if t[0]==k: result.append(t[2])
#     if t[0]>k:break
#     for i in node:
#         if i[0] ==t[2] and i[1] in city:
#             q.append([t[0]+1,i[0],i[1]])
#             city.remove(i[1])
#
# if len(result) == 0:
#     print(-1)
# else:
#     for i in result:
#         print(i)

#풀이 3 - 시간 초과
# from collections import deque
#
# def bfs(map, start,finish, visited):
#     result =[]
#     check=0
#     q=deque([start])
#     visited[start]=True
#     while q:
#         s=q.popleft()
#         check+=1
#         for i in map:
#             if i[0] == s and visited[i[1]] == False:
#                 if check == finish:
#                     result.append(i[1])
#                 q.append(i[1])
#                 visited[i[1]]=True
#         if check == finish:
#             break
#
#     return result
#
# n,m,k,x=map(int,input().split())
# map = [list(map(int,input().split())) for _ in range(m)]
# visited =[False]*(n+1)
# answer = bfs(map,x,k,visited)
# if not answer:
#     print(-1)
# else:
#     for i in answer:
#         print(i)

#풀이 4
from collections import deque
import sys
input = sys.stdin.readline # 이거 안하면 시간 초과 뜸

n,m,k,x=map(int,input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

distance=[-1]*(n+1)
distance[x]=0

q=deque([x])
while q:
    now =q.popleft()
    for i in graph[now]:
        if distance[i] == -1:
            distance[i]=distance[now]+1
            q.append(i)

check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)




