# 이진탐색
- 이진 탐색은 배열 내부의 데이터가 **정렬**되어 있어야만 사용 가능한 알고리즘
- 이진 탐색은 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 특징이 있음
- 위치를 나타내는 변수 3개 사용 - 시작점, 끝점, 중간점

  찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원한는 데이터를 찾는게 이진 탐색 과정
- 시간 복잡도 O(logN)
- 이진 탐색 구현하는 방법 **1. 재귀 함수 2. 반복문**

```
# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    #찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array,target,start,mid -1)
    #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array,target,mid + 1, end)
    
# n(우너소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int,input().split()))
# 전체 원소 입력 받기
array = list(map(int,input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0 , n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
    

# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        #찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end =  mid -1
        #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# n(우너소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int,input().split()))
# 전체 원소 입력 받기
array = list(map(int,input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0 , n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

입력 : 
10 7
1 3 5 7 9 11 13 15 17 19
출력 : 
4
```

# 이진탐색트리
- 이진 탐색 트리의 특징
  1. 부모 노드보다 왼쪽 자식 노드가 작다.
  2. 부모 노드보다 오른쪽 자식 노드가 크다.
  **왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드**
  
- 이진 탐색 트리는 입력 데이터가 많거나, 탐색 범위가 매우 넓은 편이다.
  그래서 입력 데이터가 많은 문제는 sys 라이브러리의 readline() 함수를 이용하면 시간 초과를 피할 수 있다.
  ```
  import sys
  input_data = sys.stdin.readline().rstrip()
  ```
