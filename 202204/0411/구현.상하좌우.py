
n=int(input())
direction = input().split()
location_x = 1
location_y = 1
arr =[]
temp=[]
for i in range(n):
    for j in range(n):
      temp.append(0)
    arr.append(temp)

for i in direction:

        if i == "R":
            location_y += 1
        elif i == "L":
            location_y -= 1
        elif i == "U":
            location_x -= 1
        elif i == "D":
            location_x += 1



print(arr)



