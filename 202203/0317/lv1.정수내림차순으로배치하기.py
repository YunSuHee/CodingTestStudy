# 문제 설명
# 함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

# 제한 조건
# n은 1이상 8000000000 이하인 자연수입니다.
# 입출력 예
# n	return
# 118372	873211


# run time error
def solution(n):
    answer = ''
    arr = list(str(n))
    arr.sort(reverse=True)
    for i in arr:
        answer+=i
    return int(answer)

print(solution(4564654))

# run time error
def solution(n):
    arr = list(str(n))
    arr.sort(reverse=True)
    return int(''.join(arr))

print(solution(112246546))

# 제출
def a(n):
    answer = int(''.join(sorted(str(int(n)), reverse=True)))
    return answer

print(a(465748))