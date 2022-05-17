# 동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다.
# 어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.
# 동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다.
# 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
#
# 예를 들어 가게의 부품이 총 5개일 때 부품 번호가 다음과 같다고 하자.
#
# N = 5
# [8, 3, 7, 9, 2]
#
# 손님은 총 3개의 부품이 있는지 확인 요청했는데 부품 번호는 다음과 같다.
#
# M = 3
# [5, 7, 9]
#
# 이때 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes를, 없으면 no를 출력한다. 구분은 공백으로 한다.
#
# 입력
# 첫째 줄에 정수 N이 주어진다. (1 <= N <= 1,000,000)
# 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 이때 정수는 1 보다 크고 1,000,000 이하이다.
# 셋째 줄에는 정수 M이 주어진다. (1 <= M <= 100,000)
# 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1 보다 크고 1,000,000 이하이다.
# 출력
# 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를, 없으면 no를 출력한다.

#이진탐색으로 풀기
# 시간 복잡도 부품 찾는 과정 = O(M * logN) N 부품 정렬 과정 = O(N * logN) 따라서 O((M+N) * logN)
def search (array, target, start, end):
    if start > end:
        return "no"
    mid = (start+end) // 2
    # 가운데 값이 타겟이랑 같을떄
    if array[mid] == target:
        return "yes"
    # 가운데 값이 타겟보다 클떄
    elif array[mid] > target:
        return search(array, target, start, mid -1)
    else:
        return search(array, target, mid + 1, end)
n = int(input())
n_arr= list(map(int,input().split()))
n_arr.sort()
m = int(input())
order= list(map(int,input().split()))

# order한 상품이 있는지 확인
for i in order:
    print(search(n_arr, i ,0, n-1),end=' ')

#계수 정렬로 풀기 - 계수 정렬 : 특정한 값을 가지는 데이터의 개수를 '카운트'하는 방법
#모든 원소의 번호를 포함할 수 있는 크기의 리스트를 만든 뒤에, 리스트의 인덱스에 직접 접근하여 특정한 번호의 부핌이 매장에 존재하는지 확인
n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int,input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=" ")
    else:
        print('no', end=" ")

#집합자료형 이용
#단순히 특정한 수가 한번이라도 등장했는지를 검사 - 단순히 특정한 데이터가 존재하는지 검사할 떄에 매우 효과적
#set 자료형의 containment(이게 존재하느냐. in 활용)의 복잡도는 O(1)이다 개쩐다!!!
#list의 containment 복잡도는 O(N)이니까 비교하면!!

n = int(input())
array = set(map(int,input().split()))
print(array)
m = int(input())
x = list(map(int,input().split()))

for i in x:
    if i in array:
        print('yes', end=" ")
    else:
        print('no', end=" ")

