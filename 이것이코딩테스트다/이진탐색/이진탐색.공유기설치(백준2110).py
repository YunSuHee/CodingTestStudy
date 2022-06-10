# 도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.
#
# 도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
#
# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.
#
# 출력
# 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.
#
# 예제 입력 1
# 5 3
# 1
# 2
# 8
# 4
# 9
# 예제 출력 1
# 3
# 힌트
# 공유기를 1, 4, 8 또는 1, 4, 9에 설치하면 가장 인접한 두 공유기 사이의 거리는 3이고, 이 거리보다 크게 공유기를 3개 설치할 수 없다

#메모리 초과
"""
import itertools

n,c = map(int, input().split())
home = [int(input()) for _ in range(n)]
home.sort(reverse= True)

# 공유기 조합
wifi = list(itertools.combinations(home,c))

#공유기 사이의 최소값
def distance(arr):
    min_distance=[]
    for i in range(c-1):
        min_distance.append(arr[i]-arr[i+1])
    return min(min_distance)


#인접한 공유기 사이의 최대 거리
result = 0
for i in wifi:
    temp = distance(i)
    if result < temp:
        result = temp
print(result)

"""
import sys
n,c = map(int, sys.stdin.readline().split())
home = [int(sys.stdin.readline()) for _ in range(n)]
home.sort()

start = 1
end = home[-1]-home[0]

result =[]

while start <= end:
    #공유기 사이의 최소거리
    mid = (start+end)//2

    #집 좌표에서 공유기 총 몇대 설치 가능한지
    temp = home[0] + mid
    wifi_num = 1
    for i in home:
        if i >= temp:
            temp =i+ mid
            wifi_num += 1

    #설치할수 공유기의 수가 c보다 적으면 거리가 먼거니까 줄여야함 -> end = mid-1
    if wifi_num < c:
        end = mid-1

    # 설치할수 공유기의 수가 c보다 크면 거리가 가까운거니까 start = mid+1 그리고 리스트 result 에 추가
    if wifi_num >= c:
        start = mid + 1
        result.append(mid)  # mid가 공유기 사이 gap 이니까!!!!!

print(max(result))