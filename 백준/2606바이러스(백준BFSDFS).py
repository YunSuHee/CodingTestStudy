# 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
#
# 예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자.
# 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다.
# 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.
#
#
#
# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.
#
# 출력
# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.
#
# 예제 입력 1
# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7
# 예제 출력 1
# 4
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append(x)
    result =[x]
    while queue:
        x=queue.popleft()
        for i in range(n+1):
            if graph[x][i] ==1 and i not in result:
                queue.append(i)
                result.append(i)
            graph[x][i] = 0
            graph[i][x] = 0
    return result

n=int(input())
network = int(input())
graph=[[0]*(n+1) for i in range(n+1)]

for i in range(network):
    x,y = map(int,input().split())
    graph[x][y]=1
    graph[y][x]=1
temp=[]
for i in range (n+1):
    for j in range(n+1):
        if graph[i][j] ==1:
            temp.append(bfs(i,j))
            # print('temp',temp)
            # print('graph',graph)

for i in range(len(temp)):
    if 1 in temp[i]:
        print(len(temp[i])-1)


# 다른사람 풀이
from collections import deque

N = int(input())
check = [0] * (N + 1)
Computer = [[] for _ in range(N + 1)]

for i in range(int(input())):
    a, b = map(int, input().split())
    Computer[a].append(b) #a 행에 b값을 넣어
    Computer[b].append(a)

check[1] = 1
q = deque([1]) #어차피 1 컴퓨터가 속해있는 네트워크만 보면 되니까
while q:
    x = q.popleft()
    for i in range(len(Computer[x])):
        if check[Computer[x][i]] == 0:
            q.append(Computer[x][i])
            check[Computer[x][i]] = 1 #네트워크 수 체크

print(sum(check) - 1)

