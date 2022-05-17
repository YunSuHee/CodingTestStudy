# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
#
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# completion의 길이는 participant의 길이보다 1 작습니다.
# 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# 참가자 중에는 동명이인이 있을 수 있습니다.
# 입출력 예
# participant	completion	return
# ["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
# ["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
# ["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"

# 정렬로 풀기
def solution(participant,completion):
    participant.sort()
    completion.sort()

    for p,c in zip(participant,completion):
        if p != c:
            return p
    return participant.pop()


#Hash로 풀기
def solution2(participant, completion):
    answer = ''
    sumHash = 0
    dic = {}

    #1. hash : participant의 dictionary 만들기
    #2. participant의 sum(hash) 구하기
    for part in participant:
        dic[hash(part)] = part
        sumHash += int(hash(part))
    #3. completion의 sum(hash) 빼기
    for com in completion:
        sumHash -= hash(com)
    answer = dic[sumHash]

    return answer

#counter로 풀기

import collections

def solution3(participant, completion):
    #1.participant의 counter를 구한다
    #2.completion의 counter를 구한다
    #3.둘의 차를 구하면 정답만 남아있는 counter를 반환한다
    answer = collections.Counter(participant) - collections.Counter(completion)

    #4.counter의 key값을 반환한다
    #keys를 list로 형변환 하고 이중 0번쨰 인덱스의 값을 읽어온다.
    #["A"]라는 list를 꺼내오게 되고 여기서 [0]dmfh wjqrms
    return list(answer.keys())[0]





participant =["mislav", "stanko", "mislav", "ana"]
completion =["stanko", "ana", "mislav"]

print(solution3(participant,completion))