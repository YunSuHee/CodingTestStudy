# N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다.
# 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.
#
# 입력 예시
# 2
# 홍길동 95
# 이순신 77
#
# 출력 예시
# 이순신 홍길동

n=int(input())
arr=[list(input().split()) for i in range(n)]
dic = {}
for i in arr:
    dic[i[0]]=int(i[1])

rank = sorted(dic.items(), key = lambda a : a[1])
for i in range(n):
    print(rank[i][0],end=' ')


#다른풀이
N = int(input())

array = []

for i in range(N):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))


array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')