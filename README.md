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

-set 자료형의 containment(이게 존재하느냐. in 활용)의 복잡도는 O(1)이다 개쩐다!!!
 list의 containment 복잡도는 O(N)이니까 비교하면 혁쉰 호호..
 따라서 단순히 특정한 수가 한번이라도 등장했는지를 검사 - 단순히 특정한 데이터가 존재하는지 검사할 떄에 매우 효과적

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
- **list에서 특정값의 인덱스를 찾을떄에는 index를 써야한다. find 쓰면 에러가 난다.**
    
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
    
    --------------------------------------------
    a1 = [1, 1, 1, 2, 3, 4, 5, 6]
    print(a1.index(1))
    >>> 0
    
    list_a = [1, 1, 1, 2, 3, 4, 5, 6]
    print(list_a.find(1))
    >>> AttributeError: 'list' object has no attribute 'find'
  
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
## 파이썬 문자열 합치기 join
- "구분자".join(리스트)
- 리스트 요소가 int 면 map으로 형변환 해줘야 join됨 아님 오류

```
num = [1, 3, 5, 7]
num_str = ", ".join(num)	# 에러 발생

num = [1, 3, 5, 7]
num_str = ", ".join(map(str,num))
# 1, 3, 5, 7

```
  
## 리스트 뒤에서부터 앞으로 접근 + 문자열 뒤집기
1. reversed 함수
```
array=[1,2,3]
for i in reversed(array):
    print i
```
2. slicer [::-1]
```
L = [0,10,20,40]
for i in L[::-1]:
    print i
```

## 2차원 배열
- [[0 for j in range(cols)] for i in range(rows)]
- [[0]*(cols) for i in range(rows)]
```
rows = 10
cols = 5
arr = [[0 for j in range(cols)] for i in range(rows)]
or
arr=[[0]*(cols) for i in range(rows)]

문제가 없는지 확인해보자! 🔍
이번에도 arr의 요소 하나를 골라 변경해보자.

arr[0][0] = 1
[[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
```
- [[0] * cols] * rows --> 문제 있음
```
rows = 10
cols = 5
arr = [[0] * cols] * rows

arr[0][0] = 1
[[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]

?!?!?!?!?!?! 😱
분명히 arr의 0행 0열에 대해서만 변경을 시도했는데, arr의 모든 행의 0열의 값이 변경되었다!

왜 그럴까? 🤔
Python에서는 * 연산자를 이용해 배열을 선언하게 되면, 얕은 복사(shallow copy)가 진행된다.
즉, 배열 내의 요소들이 같은 객체를 가리키게 되는 것이다.
따라서, 이 방식으로 2차원 배열을 선언하고 요소를 변경하게 되면 다른 요소들의 값도 같이 바뀌는 것이다.
```
## 정렬
### 문자열 정렬 sort(), sorted()
- sort() 리스트 메소드 정렬 (list.sort())
  변수 자체를 수정, 함수 반환값 None 값. key 서정 가능, 내림차순 가능
  ```
    arr=[1,2,5,4]
    origin = arr
    arr.sort()
    print(origin)
    print(arr)
  
    >>> [1, 2, 4, 5] 
    >>> [1, 2, 4, 5] # origin = arr
  ```
  
- sorted() 파이썬 표준 내장함수 정렬 (sorted(list))
  반환값 list 새로운 변수에 할당 가능, key 설정 가능, reverse(내림차순) 가능
  ```
    arr=[1,2,5,4]
    origin = sorted(arr)
    print(origin)
    print(arr)
  
    >>> [1, 2, 4, 5] 
    >>> [1, 2, 5, 4] # origin != arr
  ```
 ### 튜플 정렬
 ```
tuple_list = [ (3, 4), (1, 2), (2, 5) ]

위처럼 리스트의 원소가 튜플로 이루어져 있는 경우 정렬을 하기 위해서는 리스트의 sort()를 사용하면 된다.
튜플을 감싸고 있는 것이 리스트이기 때문인데 sort()의 사용법은 간단하다.

sort()의 경우 결과값을 반환해서 보여주지 않으므로 결과를 확인하기 위해서는 출력을 해주어야 한다.

tuple_list.sort()
tuple_list
>>> [(1, 2), (2, 5), (3, 4)]

튜플의 첫 번째 원소인 1,2,3 순서로 오름차순 정렬된 것을 볼 수 있다.


그 중 튜플의 첫 번째 원소를 특정해서 정렬하고 싶다면 아래와 같이 작성하며 된다

# 오름차순
tuple_list.sort(key=lambda x: x[0])

#내림차순
tuple_list.sort(key=lambda x: x[0], reverse=True)
or
tuple_list.sort(key=lambda x: -x[0])


튜플의 첫 번째 원소로 정렬, 이후 같은 값이 나오면 두 번째 원소 정렬하는 방식
tuple_list.sort(key=lambda x: (x[0], x[1]))

튜플의 두 번째 원소로 정렬, 이후 같은 값이 나오면 첫 번째 원소 정렬하는 방식
tuple_list.sort(key=lambda x: (x[1], x[0]))


오름차순, 내림차순은 reverse 혹은 - 부호를 사용하여 적절히 사용하면 된다.
```
```
첫번째 원소로 내림 차순, 두번째 원소로 오른 차순, 세번쨰 원소로 내림차순, 0번쨰 원소로 오름차순

student.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))
```

## ⭐⭐문자형 숫자 정렬
앞서 말했듯, 0로 메워진 숫자의 문자열 리스트의 경우 특별히 문제없이 정렬된다. 

0로 메워지지 않은 숫자의 문자열 리스트의 경우, 숫자로써가 아닌 **문자열을 사전순으로 나열**하므로 아래와 같은 결과가 출력되어 버리고 만다. 
아래의 예와 같이 "10"은 "5"보다 작은 것 처럼 정렬된다.

```
l = ['10', '01', '05']

print(sorted(l))
# ['01', '05', '10']

l = ['10', '1', '5']

print(sorted(l))
# ['1', '10', '5']
```


## Hash 알고리즘
- Hash는 key value의 형태를 갖는 하나의 자료구조 (전화번호부랑 똑같음)
- 해시는 공간을 좀 더 사용해 시간을 축소시키며 (공간와 시간을 맞바꾼 기법)
  데이터의 양이 어떻든 일반적인 경우 항상 O(1)을 기대할 수 있습니다.
  해시는 특정 키(key)를 해시 함수를 통해 해시 테이블의 주소값으로 변경합니다.
  **따라서. hashDict[hash("수희")] = 1 면 print(hashDict) 하면 {968578591888283667: 1}로 결과가 나옴**
- 언제 해시 알고리즘을 사용하는가?
  String을 기반으로 정보를 기록하고 관리해야 될 때 (Key가 String)
  
## Counter
-데이터의 개수를 셀 때 유용한 파이썬의 collections 모듈의 Counter 클래스
-Python이 제공하는 collections라는 모듈의 한 class
-list를 가지고 Counter를 생성하면, Counter는 Key가 이름이고, Value가 count인 dictionary를 반환

```
import collections

participant=["A","B"]
answer = collections.Counter(participant)
print(answer) # 결과 : Counter({'A': 1, 'B': 1})
print(list(answer.keys())) # 결과 : ['A', 'B']
print(list(answer.keys())[0])  # 결과 : A
print((answer.keys()))  # 결과 : dict_keys(['A', 'B'])
print(list(answer))  # 결과 : ['A', 'B']
print(list(answer.values()))  # 결과 : [1, 1]
```
 
## 리스트의 숫자 문자열 -> 숫자 // 숫자 -> 문자열
```
n=[1,2,3,4]
n = list(map(str, n))
```

## array[-1]

```
array=[1,2]
print(array[-1])   
# 결과 2
```
## list 복사 방법
1) 슬라이싱Permalink
```
>>> list1 = [1, 2, 3, 4]
>>> list2 = list1[:]

```
시작점과 끝점을 생략한 슬라이싱은 리스트의 모든 요소를 뜻한다. 슬라이싱을 통해 변수를 정의하면 파이썬은 새로운 객체를 만든다.

2) list() 함수Permalink
```
>>> list1 = [1, 2, 3, 4]
>>> list2 = list(list1)```
```
파이썬 내장함수 중에는 iterable한 객체를 리스트 객체로 변환해주는 list() 함수가 있다. 이 함수를 이용해 복사하고자 하는 리스트 객체를 다시 재선언 한다.

3) copy() 메소드Permalink
```
>>> list1 = [1, 2, 3, 4]
>>> list2 = list1.copy()
```
Python3 부터 리스트를 다른 리스트에 복사하는 기능인 copy() 메소드가 추가되었다. 가독성을 위한 코드라면 이 방법을 사용하는 것을 권장한다.

4) 리스트 연산Permalink
```
>>> list1 = [1, 2, 3, 4]
>>> list2 = [] + list1
```
리스트 덧셈연산을 이용해 새로운 빈 리스트에 list1의 요소들을 더한다. 새로운 리스트 객체에 list1의 요소들이 더해져 결과적으로 우리가 원하는 복사가 이뤄진다.

**append 할 경우엔 list1과 list2가 별개로 보이지만 요소 값을 바꾸면 둘다 바뀐다. 이때는 deepcopy()메소드를 사용해야한다**
**list2 = copy.deepcopy(list1)**

