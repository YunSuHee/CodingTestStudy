# a,m,d,n=input().split()
# a=int(a)
# m=int(m)
# d=int(d)
# n=int(n)

# for i in range (2,n+1):
#     a = a*m+d
    
# print(a)

# n = int(input())
# a=input().split()
# t=[]

# for i in range(n):
#     a[i] = int(a[i])

# for i in range(23) :  
#   t.append(0)     
# for i in range(23):
#     for j in range (n):
#         if a[j] == i+1:
#             t[i]+=1
#         else :
#             continue


# for i in t:
#     print(i, end=' ')

# n= int(input())
# a=input().split()
# for i in range (n):
#     a[i]=int(a[i])

# a.sort()
# print(a[0])

# n=int(input())
# a=[]
# for i in range (19):
#     a.append([])
#     for j in range (19):
#         a[i].append(0)

# for i in range (n):
#     x,y = input().split()
#     a[int(x)-1][int(y)-1] =1
     
# for i in a:
#     for j in i:
#         print(j, end=' ')
#     print()
    

##################
# n=[]
# for i in range (19):
#     n.append([])
#     for j in range(19):
#         n[i].append(0)

# for i in range(19):
#     x=input().split()
#     for j in range(19):
#         n[i][j]=int(x[j])

# a = int(input())
# for i in range(a):
#     x,y = input().split()
#     x=int(x)-1
#     y=int(y)-1
#     first=n[x][y]
#     for i in range(19):
#         if n[x][i]==1:
#             n[x][i]=0
#         elif n[x][i]==0:
#             n[x][i]=1
        
#         if n[i][y]==1:
#             n[i][y]=0
#         elif n[i][y]==0:
#             n[i][y]=1
    
#     n[x][y]=first       
        
# for i in n:
#     for j in i:
#         print(j, end=' ')
#     print()


##################
# h, w =input().split() # h = 세로 w = 가로
# n=int(input())
# h=int(h)
# w=int(w)
# t=[]
# for i in range(h):
#     t.append([])
#     for j in range(w):
#         t[i].append(0)

# for i in range(n):
#     l,d,x,y=input().split()
#     l=int(l); d=int(d); x=int(x); y=int(y);
#     if d==0:
#         for i in range(l):
#             t[x-1][y-1+i]=1
#     else: 
#         for i in range(l):
#             t[x-1+i][y-1]=1
    
# for i in t:
#     for j in i:
#         print(j, end=' ')
#     print()


#########################

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



