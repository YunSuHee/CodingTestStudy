# 집에서 시간을 보내던 오영식은 박성원의 부름을 받고 급히 달려왔다. 박성원이 캠프 때 쓸 N개의 랜선을 만들어야 하는데 너무 바빠서 영식이에게 도움을 청했다.
#
# 이미 오영식은 자체적으로 K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이다.
# 박성원은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다. 예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm는 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)
#
# 편의를 위해 랜선을 자르거나 만들 때 손실되는 길이는 없다고 가정하며, 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자.
# 그리고 자를 때는 항상 센티미터 단위로 정수길이만큼 자른다고 가정하자. N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에는 오영식이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력된다.
# K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다. 그리고 항상 K ≦ N 이다. 그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 정수로 입력된다. 랜선의 길이는 231-1보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다.
#
# 예제 입력 1
# 4 11
# 802
# 743
# 457
# 539
# 예제 출력 1
# 200

import sys


def solution():
    K, N = map(int, input().split())
    # sys.stdin.readline() 사용이유는 글 하단 참고
    lan = [int(input()) for _ in range(K)]

    min_value = 1  # 랜선의 최소 길이를 1로 설정
    max_value = max(lan)  # 랜선중 가장 긴 길이를 max값으로 설정

    while min_value <= max_value:  # 이분탐색이 완료될때까지 반복
        mid = (min_value + max_value) // 2  # 이분탐색을 위한 중간값 설정
        cnt = 0  # 랜선 수를 카운팅하는 변수 반복될때 마다 초기화 해야 하므로 반복문 안에서 선언
        for i in lan:
            cnt += i // mid  # 랜선을 자른 수

        if cnt >= N:  # 랜선을 자른 수가 만들어야될 랜선의 수보다 클 경우
            min_value = mid + 1  # 랜선의 최소 길이를 중간값보다 1크게 설정
        else:  # 랜선을 자른 수가 만들어야될 랜선의 수보다 작을 경우
            max_value = mid - 1  # 랜선의 최대 길이를 중간값보다 1작게 설정

    return max_value  # 랜선을 자룬 수가 만들어야 될 랜선의 수와 같을경우 길이 출력


print(solution())