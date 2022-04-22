# 파이썬 자료구조, 함수

[딕셔너리](#딕셔너리dict)

[count 함수](#count-함수)

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
   ### 이중 리스트 중복 제거
   - list 안에 있는 list를 tuple로 변환하고 set으로 다시 중복 제거 하기
   - set(list(map(tuple,[[9, 9], [], [], [9, 9]])))
    

## find, index 함수 - 인덱스, 위치를 찾는 함수

- 변수.find(찾을문자) -> 문자열 위치 출력
- 변수.index(찾을문자) -> 문자열 위치 출력
    
    ### find, index 함수 차이점
    - find : 찾는 문자가 없는 경우에 **-1**을 출력한다. 
             문자열을 찾을 수 있는 변수는 **문자열만 사용이 가능**하다.  리스트, 튜플, 딕셔너리 자료형에서는 find 함수를 사용할 수 없다. 만일 사용하게 되면 AttributeError 에러가 발생한다.
    - index : 찾는 문자가 없는 경우에 ValueError 에러가 발생한다.
              **문자열, 리스트, 튜플 자료형에서 사용 가능**하고 딕셔너리 자료형에는 사용할 수 없어 AttributeError 에러가 발생한다.
      
      
    ``` 
  
    # 문자열중 2번째 위치부터 처음 'x'가 위치한 자리
    >>> 'oxoxoxoxox'.index('x', 2)
    3
    
    # a변수에서 1번째~3번째 사이에 문자 'o'가 위치한 자리
    >>> a = 'hello'
    >>> a.find('o', 1, 3)
    -1	
    # find함수는 찾는 값이 없을 때 -1을 출력한다.
  
    ```
   
## 딕셔너리(dict)

- 대응 관계를 나타낼 수 있는 자료형, 연관 배열 또는 해쉬라고 함
- key와 value를 한쌍으로 갖는 자료형
- {key1: value1, key2: value2, ...}
- **키 값에 list,set이 올 수 없다** - 키 값은 불변한 객체 타입이 와야한다
- **키 값은 중복 될 수 없다** - 동일한 키를 추가하면 나중에 추가된 키와 값에 기존의 키와 값이 덮어띄워집니다.
키 값은 고유해야하기 때문입니다. 그래야 정확히 그 데이터에 접근할 수 있기 때문입니다.

    ### 딕셔너리 쌍 추가, 삭제
    - 딕셔너리[키] = 값 을 통해서 키,값 쌍을 추가
    - 딕셔너리[키] 를 통해서 값에 접근
    - 딕셔너리[키] = 값 을 통해서 값을 변경

    ```
    # 1. 딕셔너리 생성
    d = {'a': 123123}
    
    # 2. 값 추가
    d[999] = 10  # 숫자 키, 숫자 값
    d['99'] = 111  # 문자 키, 숫자 값
    d['BlockDMask'] = "blog"  # 문자 키, 문자 값
    d['wow'] = [1, 2, 3, 4, 5]  # 문자 키, 리스트 값
    d[(1, 2)] = "this is value"  # 튜플 키, 문자 값
    d[1] = (3, 'a', 5)  # 숫자 키, 튜플 값
    
    print(d)
    
    >> {'a': 123123, 999: 10, '99': 111, 'BlockDMask': 'blog', 'wow': [1, 2, 3, 4, 5], (1, 2): 'this is value', 1: (3, 'a', 5)}
    ```
    ### 딕셔너리 사용 법 
    ```
    >>> a = {'a':1, 'b':2}
    >>> a['a']
    1
    >>> a['b']
    2
    ```
    ### 딕셔너리 관련 함수 (keys(), values(), items(), del(), clear(), get(), in)
    ```
    # keys()
    d = {'a': 123123, 'kim': 'blockdmask', 'b': "blog", 'c': 3333, 123: 'name'}
    
    # keys()
    print(d.keys())
    
    >>> dict_keys(['a', 'kim', 'b', 'c', 123])
    
    # values()
    print(d.values())
    
    >>> dict_values([123123, 'blockdmask', 'blog', 3333, 'name'])
    
    # items()
    print(d.items())
    
    >>> dict_items([('a', 123123), ('kim', 'blockdmask'), ('b', 'blog'), ('c', 3333), (123, 'name')])
    # get()- 값이 없을때
    r1 = d.get('ccc')
    print(f"d.get('ccc') : {r1}")
    
    >>> d.get('ccc') : None
    
    # get()- 값이 있을때
    r3 = d.get('a')
    print(f"d.get('a') : {r3}")
    
    >>> d.get('a') : 123123
    ```
  ### dict 정렬
  - key 기준 정렬
  ```
    my_dict = {'c': 3, 'a': 1, 'b': 2, 'e': 1, 'd': 2}
    
    #오름차순
    sorted_dict = sorted(my_dict.items())
    print(sorted_dict)
    
    >>> [('a', 1), ('b', 2), ('c', 3), ('d', 2), ('e', 1)]
    
    #내림차순
    sorted_dict = sorted(my_dict.items(), key = lambda item: item[0], reverse = True)
    print(sorted_dict)
    
    >>> [('e', 1), ('d', 2), ('c', 3), ('b', 2), ('a', 1)]
  ```
  - value 기준 정렬
  ```
    my_dict = {'c': 3, 'a': 1, 'b': 2, 'e': 1, 'd': 2}
    
    #오름차순
    sorted_dict = sorted(my_dict.items(), key = lambda item: item[1])
    print(sorted_dict)
    
    >>> [('a', 1), ('e', 1), ('b', 2), ('d', 2), ('c', 3)]
    
    #내림차순
    sorted_dict = sorted(my_dict.items(), key = lambda item: item[1], reverse = True)
    print(sorted_dict)
    
    >>> [('c', 3), ('b', 2), ('d', 2), ('a', 1), ('e', 1)]
  ```
## lambda 함수
- 이름없는 함수, 람다표현식을 익명함수라 함  
![image](https://user-images.githubusercontent.com/97869193/164709759-aba5cd56-99a4-4a6b-a77c-fe04e6400164.png)

```
f= lambda x:x+10
print(f(10))

>>> 20

```
## count 함수 

- count( ) 문자열의 개수, 리스트의 개수 세는 함수 (Python)

    ```
    >>> 'ooyyy'.count('y')
    3
    
    >>> a = [1, 1, 1, 2, 3]
    >>> a.count(1)
    3
    
    >>> ['ox', 'o', 'x', 'oxoxox'].count('ox')
    1
    ```

  
