# "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
#
# 단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력하는 프로그램을 작성하라.
from collections import deque

for k in range(1,int(input())+1):
    print("#%d"%k,end=" ")
    word = input()
    n = int(len(word)/2)
    answer=0
    queue = deque()
    for i in range(n):
        queue.appendleft(word[i])

    if len(word)%2 ==0:
        for j in range(n,len(word)):
            if queue.popleft()==word[j]:
                answer+=1
        if answer == n:
            print(1)
        else:
            print(0)
    else:
        for j in range(n+1,len(word)):
            if queue.popleft()==word[j]:
                answer+=1
        if answer == n:
            print(1)
        else:
            print(0)

