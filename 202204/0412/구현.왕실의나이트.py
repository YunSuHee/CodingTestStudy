loc = input()
row = int(loc[1])
col = int(ord(loc[0]))-ord('a')+1

move = [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
result = 0
for i in move:
    x = col+i[0]
    y = row+i[1]
    if x<1 or x>8 or y<1 or y>8:
        continue
    result+=1
print(result)