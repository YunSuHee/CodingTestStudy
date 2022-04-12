
n=int(input())
direction = input().split()

move = ['L','R','U','D']
x = [0,0,-1,1]
y = [-1,1,0,0]
mx = 1
my = 1
temp = 0
for i in direction:
    for j in range(4):
        if i == move[j]:
            temp = j
            mx += x[j]
            my += y[j]
    if mx <1 or my<1 or mx>n or my>n:
        mx -= x[temp]
        my -= y[temp]
print(mx, my)
