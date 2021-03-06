# 문제
# N개의 동전이 주어질 때, 이 동전들로 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에는 동전의 개수를 나타내는 양의 정수 N이 주어진다. (1 <= N <= 1,000)
# 둘째 줄에는 각 동전의 화폐 단위를 나타내는 N개의 자연수가 주어지며 각 자연수는 공백으로 구분된다. 각 화폐 단위는 1,000,000 이하의 자연수이다.
#
# 출력
# 첫째 줄에 주어진 동전들로 만들 수 없는 양의 정수 금액 중 최솟값을 출력한다.


n = int(input())
coin = list(map(int,input().split()))
coin.sort()
target = 1

for i in coin:
    if target >= i:
        target+=i
    else:
        break

print(target)