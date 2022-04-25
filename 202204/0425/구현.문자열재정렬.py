# 문제
# 알파벳 대문자와 숫자 (0~9)로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에,
# 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
# 예를 들어 K1KA5CB7이 입력으로 들어오면, ABCKK13을 출력합니다.
#
# 입력:
# K1KA5CB7
# FDSARQWER13579
#
# 출력:
# ABCKK13
# ADEFQRRSW25

n=input()
answer=[]
num=0
result=''
for i in range(len(n)):
    answer.append(n[i])
answer.sort()
for i in answer:
    if ord(i) >=48 and ord(i)<=57:
        num+=int(i)
    else :
        result+=i
print(result+str(num))

#답안 예시
data = input()
result = []
value=0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value+=int(x)
result.sort()

if value != 0:
    result.append(str(value))
print(''.join(result))