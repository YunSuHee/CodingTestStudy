# 문제 설명
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

# 제한 조건
# n은 10,000,000,000이하인 자연수입니다.
# 입출력 예
# n	return
# 12345	[5,4,3,2,1]

#1 -> run time error
def solution(n):
    answer =  list(map(int,sorted(list(str(n)),reverse=True)))

    return answer


#2 -> run time error
def solution(n):
    answer = sorted(list(str(n)),reverse=True)

    return [int(i) for i in answer]

#3 다른 사람 풀이
def solution(n):
    	return [int(i) for i in str(n)][::-1]
 
#4 다른사람 풀이
def solution(n):
    	return list(map(int, reversed(str(n))))

print(solution(12345))