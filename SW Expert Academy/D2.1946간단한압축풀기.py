# 압축된 문서의 내용
#
# A 10
# B 7
# C 5
#
#
# 압축을 풀었을 때 원본 문서의 내용
#
# AAAAAAAAAA
# BBBBBBBCCC
# CC
#
#
# [제약사항]
#
# 1. 압축된 문서의 알파벳과 숫자 쌍의 개수 N은1이상 10이하의 정수이다. (1 ≤ N ≤ 10)
#
# 2. 주어지는 알파벳 Ci는 A~Z의 대문자이다. (i는 줄의 번호로 1~N까지의 수)
#
# 3. 알파벳의 연속된 개수로 주어지는 수 Ki는 1이상 20이하의 정수이다. (1 ≤ Ki ≤ 20, i는 줄의 번호로 1~N까지의 수)
#
# 4. 원본 문서의 너비는 10으로 고정이다.
#
#
# [입력]
#
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
#
# 각 테스트 케이스에는 N이 주어지고 다음 줄부터 N+1줄까지 Ci와 Ki가 빈 칸을 사이에 두고 주어진다.
#
#
# [출력]
#
# 각 줄은 '#t'로 시작하고, 다음 줄부터 원본 문서를 출력한다.
#
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
testcase=int(input())
for k in range(1,testcase+1):
    n =int(input())
    temp=""
    for i in range(n):
        alph , num = input().split()
        temp+=alph*int(num)
    print('#%d'%k)
    n = 0
    while n <len(temp):
        print(temp[0+n:10+n])
        n+=10


#다른 풀이
# testcase=int(input())
# n =int(input())
# temp=""
# for i in range(n):
#     alph , num = input().split()
#     temp+=alph*int(num)
# print('#%d'%testcase)
# n = 0
# for i in range(1,len(temp)+1):
#     if i % 10 !=0:
#         print(temp[i-1],end="")
#     else:
#         print(temp[i-1])