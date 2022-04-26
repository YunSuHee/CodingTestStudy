n=int(input())

coin_type = [500, 100, 50,10]
count = 0

for coin in coin_type:
    count += n //coin
    n%= coin

print(count)