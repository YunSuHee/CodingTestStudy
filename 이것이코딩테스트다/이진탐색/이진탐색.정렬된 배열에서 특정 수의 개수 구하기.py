# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다. 이때 이 수열에서 x가 등장하는 횟수를 계산하세요.
# 단, 이 문제의 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 '시간 초과' 판정을 받습니다.
#
# a. 예를 들면.
# 수열 {1, 1, 2 ,2 ,2 ,2, 3}이 있을 때 x=2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력한다.
#
# b. 입력 조건
# 첫째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력된다.
# 1 <= N <= 1,000,000
# -1e9 <= x <= 1e9
# 둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력된다
# -1e9 <= 각 원소의 값 <= 1e9
# c. 출력 조건
# 수열의 원소 중에서 값이 x인 원소의 개수를 출력한다. 단 값이 x인 원소가 하나도 없다면 -1일 출력한다.
#
# d. 테스트 케이스
# 입력 예시
# 7 2
# 1 1 2 2 2 2 3
# 출력 예시
# 4

# 입력 예시
# 7 4
# 1 1 2 2 2 2 3
# 출력 예시
# -1

# 입력 예시
# 10 4
# 1 2 3 3 3 3 3 3 4 5
# 출력 예시
# 1

#이진 탐색
def start_binary(arr, start, end, target): #while문으로 이진 탐색 풀기
    while start <= end:
        mid = (start+end)//2

        if arr[mid] == target and arr[mid-1] != target: #(mid ==0 or target > array[mid-1]) and array[mid] == target 도 가능
            return mid
        elif arr[mid] < target:
            start = mid+1
        else:
            end = mid -1
    return -1

def end_binary(arr, start, end, target): #재귀로 이진 탐색 풀기
    if start > end:
        return -1
    mid = (start+end)//2

    if arr[mid] == target and (mid + 1 == len(arr) or arr[mid + 1] != target):  # arr[mid] == target and (arr[mid + 1] != target or mid+1 == len(arr))
        return mid                                                              # 이렇게 쓰면 에러 arr[mid+1] 이거가 마지막 값을 확인 할떄 list out of range 에러 뜸   mid+1 == len(arr) 먼저 해줘야 함

    if arr[mid] <= target:
        return end_binary(arr, mid+1, end,target)
    else:
        return end_binary(arr, start, mid-1, target)



n, target = map(int,input().split())
arr = list(map(int,input().split()))

start = start_binary(arr, 0, n-1, target)

if start == -1:  # x의 원소가 없음
    print(-1)
else:            # x의 원소가 있음
    end = end_binary(arr,0, n-1, target)
    print(end - start +1)

#이진탐색 라이브러리 bisect 활용가능

from bisect import bisect_right, bisect_left

n, target = map(int,input().split())
arr = list(map(int,input().split()))

def count(array, left, right):
    left_index = bisect_left(array,left)
    right_index = bisect_right(array,right)
    return right_index-left_index

result = count(arr,target,target)
if result == 0:
    print(-1)
else:
    print(result)

