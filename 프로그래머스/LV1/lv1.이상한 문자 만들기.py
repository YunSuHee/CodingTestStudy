# 문제 설명
# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
# 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.
#
# 제한 사항
# 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
# 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.
# 입출력 예
# s	return
# "try hello world"	"TrY HeLlO WoRlD"
# 입출력 예 설명
# "try hello world"는 세 단어 "try", "hello", "world"로 구성되어 있습니다. 각 단어의 짝수번째 문자를 대문자로,
# 홀수번째 문자를 소문자로 바꾸면 "TrY", "HeLlO", "WoRlD"입니다. 따라서 "TrY HeLlO WoRlD" 를 리턴합니다.

def solution(s):
    answer = ''
    a = s.split(" ")
    for i in range(len(a)):
        word = list(a[i])
        for j in range(len(word)):
            if j % 2 == 0:
                word[j] = word[j].upper()
            else:
                word[j] = word[j].lower()
        a[i] = "".join(word)
    answer = " ".join(a)

    return answer

print(solution(" aa bb cc ddd   "))

# 다른사람 풀이
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

# 다른 풀이
def toWeirdCase(s):
    liste = []
    for i in s.split():
        result = ''
        for n,v in enumerate(i):
            if n%2 == 0:
                result += v.upper()
            else:
                result += v.lower()
        liste.append(result)
    return ' '.join(liste)

# 다른사람 풀이
