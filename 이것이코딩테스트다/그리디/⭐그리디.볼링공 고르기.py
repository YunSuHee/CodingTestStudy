# A, B 두 사람이 볼링을 치고 있습니다. 두 사람은 서로 무게가 다른 볼링공을 고르려고 합니다.
# 볼링공은 총 N개가 있으며 각 볼링공마다 무게가 적혀 있고, 공의 번호는 1번부터 순서대로 부여됩니다.
# 또한 같은 무게의 공이 여러 개 있을 수 있지만, 서로 다른 공으로 간주합니다. 볼링공의 무게는 1부터 M까지의 자연수 형태로 존재합니다.


n, m = map(int, input().split())
ball = list(map(int, input().split()))

result = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        if ball[i] == ball[j]:
            continue
        else:
            result += 1

print(result)

# 그리디 풀이
n, m = map(int, input().split())
ball = list(map(int, input().split()))

arr =[0]*11
result=0
for i in ball:
    arr[i] += 1

for i in range(1,m+1):
    n-=arr[i]
    result+= arr[i]*n
print(result)

