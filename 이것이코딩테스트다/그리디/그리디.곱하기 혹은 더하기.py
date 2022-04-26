# 여러개의 숫자로 구성된 하나의 문자열 s를 입력받음
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 'x' 혹은 '+' 연산자를 넣어
# 만들어질 수 있는 가장 큰 수를 구하시오
# 단, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정

s = input()
arr = list(map(int,s))

result = 0
for i in arr:
    if result ==0 or i ==0:
        result+=i
    else:
        result *=i

print(result)