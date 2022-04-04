# 문제

#'큰 수의 법칙'은 일반적으로 통계 분야에서 다루어지는 내용이지만 동빈이는 본인만의 방식으로 다르게 사용하고 있다.

# 동빈이의 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
#
# 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.
#
# 예를 들어 순서대로 2, 4, 5, 4, 6으로 이루어진 배열이 있을 때 M이 8이고, K가 3이라고 가정하자.
#
# 이 경우 특정한 인덱스의 수가 연속해서 세 번까지만 더해질 수 있으므로 큰 수의 법칙에 따른 결과는
#
# 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 인 46이 된다.


# n,m,k = map(int,input().split())
# arr = list(map(int,input().split()))
# arr.sort(reverse=True)
#
# result =0
# if arr[0] == arr[1]:
#     result = arr[0]*m
#
# else:
#     multi = int(m/(k+1))
#     sum = m%(k+1)
#     result = (arr[0]*k+arr[1])*multi + (arr[0]*sum)
#
# print(result)


n, m, k = map(int,input().split())
data = list(map(int,input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]

answer = 0

while m!=0 :
    for i in range(k) :
        answer += first
        m -= 1

    answer += second
    m -= 1

print(answer)


