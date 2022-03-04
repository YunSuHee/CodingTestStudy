t=[]
for i in range(10):
    t.append([])
    for j in range(10):
        t[i].append(0)

for i in range(10):
    a = input().split()
    for j in range(10):
        t[i][j]=int(a[j])
        
def fun():
    k=1
    for i in range(1,9):
            for j in range(k,9):
                if t[i][j]==2 or (t[i+1][j]==1 and t[i][j+1]==1) or (i==8 and j==8) :
                    t[i][j]=9
                    return
                
                t[i][j]=9
                if t[i][j+1]==0 or t[i][j+1]==2:
                    continue
                else:
                    k=j
                    break        
                    
fun()
for i in t:
    for j in i:
        print(j, end=' ')
    print()