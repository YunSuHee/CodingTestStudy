# 오늘 동빈이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했다. 오늘은 떡볶이 떡을 만드는 날이다.
# 동빈이네 떡볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않다. 대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.
# 절단기의 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다. 높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고,
# 낮은 떡은 잘리지 않는다. 이걸 처리 안 해줘서 시간을 허비했다.
# 예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될 것이다.
# 잘린 떡의 길이는 차례대로 4, 0, 0, 2cm이다. 손님은 6cm만큼의 길이를 가져간다.
# 손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.
#
# <제한 사항>
# 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다. (1<=N<=1,000,000, 1<=M<=2,000,000,000)
# 둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M 이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다.
# 높이는 10억보다 작거나 같은 양의 정수 또는 0이다.
#
# <입력 예시>
# 4 6
# 19 15 10 17
#
# <출력 예시>
# 15
#
def search(arr, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        result = 0
        for i in arr:
            if (i - mid) > 0:
                result += (i-mid)
        if result == target:
            return mid
        elif result > target:
            start = mid+1
        else:
            end = mid -1

n,target = map(int,input().split())
arr = list(map(int,input().split()))

print(search(arr,target,1,max(arr)))

#전형적인 이진 탐색 문제이자 파라메트릭 서치 유형의 문제입니다. 파라메트릭 서치는 최적화 문제를 결정 문제로 바꾸어 해결하는 기법입니다.
# 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제에 주로 파라메트릭 서치를 사용한다.
# 이 문제의 풀이 아이디어는 의외로 간단한데 적절한 높이를 찾을 때까지 절단기의 높이 H를 반복해서 조정하는 것이다.
# 그래서 '현재 이 높이로 자르면 조건을 만족할 수 있는가?'를 확인한 뒤에 조건의 만족 여부('예' 혹은 '아니오')에 따라서 탐색 범위를 좁혀서 해결할 수 있다.
# 범위를 좁힐 때는 이진 탐색의 원리를 이용하여 절반씩 탐색 범위를 좁혀 나간다.

#풀이 아이디어는 적절한 높이를 찾을 때까지 절단기의 높이를 반복해서 조정하는 것입니다.

#파라메트릭 서치 문제 유형은 이진탐색을 재귀적으로 구현하지 않고 반복문을 이용해 구현


