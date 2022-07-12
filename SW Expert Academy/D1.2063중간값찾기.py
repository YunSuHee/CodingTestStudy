#중간값 구하기
n = int(input())
num = list(map(int,input().split()))

middle=int((n/2))
num.sort()
print(num[middle])