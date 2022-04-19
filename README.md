# 파이썬 자료구조, 함수


## rjust, ljust 함수

- rjust( n , c=' ') : 문자열을 오른쪽으로 n만큼 정렬함. 빈칸은 c로 채워 넣는다.

- ljust( n , c=' ') : 문자열을 왼쪽으로 n만큼 정렬함. 빈칸은 c로 채워 넣는다.
```
a="abc"

print(a.rjust(10))

print(a.rjust(10,'#'))

b="def"

print(a.ljust(15))

print(a.ljust(15,'k'))

>>> 결과
       abc
#######abc
abc            
abckkkkkkkkkkkk
```

## set(집합) 자료형

- 순서 없다
- 고유한 값을 가진다(중복 불가능)     
**따라서 set(리스트) 하면 리스트 값중 중복되는 값 제거해줌**
- 교집합, 합집합, 차집합을 구할 수 있다.
```
s1 = set([1, 2, 3, 4, 5])
s2 = set([4, 5, 6, 7, 8])
 
# 교집합 메서드 intersection
print(s1.intersection(s2))
 
# 교집합 연산자 &
print(s1 & s2)

>>> 결과
{4, 5}
{4, 5} 

# 합집합 메서드 union
print(s1.union(s2))
 
# 합집합 연산자 |
print(s1 | s2)

>>> 결과
{1, 2, 3, 4, 5, 6, 7, 8}
{1, 2, 3, 4, 5, 6, 7, 8}

# 차집합 메서드 difference
print(s1.difference(s2))
print(s2.difference(s1))
 
# 차집합 연산자 -
print(s1 - s2)
print(s2 - s1)

>>> 결과
{1, 2, 3}
{8, 6, 7} 
{1, 2, 3}
{8, 6, 7} 

```