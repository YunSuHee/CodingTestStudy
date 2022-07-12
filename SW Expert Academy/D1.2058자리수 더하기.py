# 각 자릿수 합 계산
n=input()
sum=0
for i in range(len(n)):
    sum += int(n[i])

print(sum)