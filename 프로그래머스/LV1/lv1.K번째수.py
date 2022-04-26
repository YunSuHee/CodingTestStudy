# 제한사항
# array의 길이는 1 이상 100 이하입니다.
# array의 각 원소는 1 이상 100 이하입니다.
# commands의 길이는 1 이상 50 이하입니다.
# commands의 각 원소는 길이가 3입니다.
# 입출력 예
# array	commands	return
# [1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]
# 입출력 예 설명
# [1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.
# [1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는 6입니다.
# [1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        arr = commands[i]
        start = arr[0]-1
        end = arr[1]
        result=arr[2]-1
        arr2=array[start:end]
        arr2.sort()
        answer.append(arr2[result])
    return answer

# 다른사람 풀이
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command  #i,j,k 한번에 변수로 지정....굿
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer

# 대단
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

