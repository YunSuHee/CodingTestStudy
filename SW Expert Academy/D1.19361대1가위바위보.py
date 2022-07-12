#가위 1 , 바위 2 보 3
# 이기는 경우 판별

A,B = map(int,input().split())

if (A <B):
    if (A ==1 and B==3):
        print('A')
    else:
        print('B')
else:
    if (B ==1 and A==3):
        print('B')
    else:
        print('A')

# 다른 사람 코드
A, B = map(int, input().split())

xyz = {1: 3, 2: 1, 3: 2}

if xyz[A] == B:

    print("A")

else:

    print("B")