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
 <span style="color:yellow">따라서 set(리스트) 하면 리스트 값중 중복되는 값 제거해줌</span>
