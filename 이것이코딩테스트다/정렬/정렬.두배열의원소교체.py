# 동빈이는 두 개의 배열 A와 B를 가지고 있다. 두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는
# 모두 자연수이다
#
# 동빈이는 최대 K 번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 A에 있는 원소 하나와
# 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말한다
#
# 동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이며, 여러분은 동빈이를 도와야한다
#
# N, K, 그리고 배열 A와 B의 정보가 주어졌을 때, 최대 K 번의 바꿔치기 연산을 수행하여 만들 수 있는
# 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하라
#
# 예를 들어 N = 5, K = 3이고, 배열 A와 B가 다음과 같다고 해보자
#
# 배열 A = [1, 2, 5, 4, 3]
#
# 배열 B = [5, 5, 6, 6, 5]
# 이 경우, 다음과 같이 세 번의 연산을 수행할 수 있다
#
# 연산 1) 배열 A의 원소 '1'과 배열 B의 원소 '6'을 바꾸기
#
# 연산 2) 배열 A의 원소 '2'와 배열 B의 원소 '6'을 바꾸기
#
# 연산 3) 배열 A의 원소 '3'과 배열 B의 원소 '5'를 바꾸기
# 세 번의 연산 이후 배열 A와 배열 B의 상태는 다음과 같이 구성될 것이다
#
# 배열 A = [6, 6, 5, 4, 5]
#
# 배열 B = [3, 5, 1, 2, 5]
# 이때 배열 A의 모든 원소의 합은 26이 되며, 이보다 더 합을 크게 만들 수는 없다
#
# 입력
# 첫 번째 줄: N, K 가 공백으로 구분되어 입력 (1 <= N <= 100,000, 0 <= K <= N)
# 두 번째 줄: 배열 A의 원소들이 공백으로 구분되어 입력 (원소 a < 10,000,000인 자연수)
# 세 번째 줄: 배열 B의 원소들이 공백으로 구분되어 입력 (원소 b < 10,000,000인 자연수)
# 출력
# 최대 K번 바꿔치기 연산을 수행해서 가장 최대의 합을 갖는 A의 모든 원소 값의 합을 출력
# 입력 예시
#
# 5 3
# 1 2 5 4 3
# 5 5 6 6 5
# 출력 예시
#
# 26

# 틀림
n, k =map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))

arr1.sort()
arr2.sort()
k_count=0
for i in range(n):
    if k_count == k:
        break
    arr1[i],arr2[n-i-1]=arr2[n-i-1],arr1[i]
    k_count+=1
print(arr1)
print(arr2)
print(sum(arr1))

# 다른사람풀이
n, k =map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))

arr1.sort()
arr2.sort(reverse=True)

for i in range(k):
    if arr1[i]<arr2[i]:
        arr1[i],arr2[i]=arr2[i],arr1[i]  #스위치
    else:
        break
print(arr1)
print(arr2)
print(sum(arr1))