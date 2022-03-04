a, b = map(int, input().strip().split(' '))

for i in range (b):
    for j in range(a):
        print('*',end='')
    print()
print(a + b)
print(('*'*a+'\n')*b)
# print(('*'*a+'\n')*b) 해도됨

