# 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.
#
# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다.
# A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.
#
# 입력
# 첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.
#
# 출력
# A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.
#
# 예제 입력 1
# 2 162
# 예제 출력 1
# 5

# 2 → 4 → 8 → 81 → 162

# 예제 입력 2
# 4 42
# 예제 출력 2
# -1

# 예제 입력 3
# 100 40021
# 예제 출력 3
# 5

# 100 → 200 → 2001 → 4002 → 40021


#bfs
from collections import deque
A,B=map(int,input().split())

queue=deque()
queue.append((A,1)) # 이렇게 넣어야 deque([(2,1)])이렇게 값이 나와서 popleft가 가능해짐

answer=0
while queue:
    a, now =queue.popleft()
    if a == B:
        answer = now
        break
    if a> B:
        continue
    queue.append((a*2,now+1))
    queue.append((int(str(a)+'1') , now + 1))
print(-1 if answer==0 else answer)





























