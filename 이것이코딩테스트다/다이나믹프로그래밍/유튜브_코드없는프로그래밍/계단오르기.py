
#문제 : i번째 계단을 오르는 비용이 cost[i]로 주어졌다. 계단을 한번에 한칸 혹은 두칸씩만 오를수 있을때, 전체 계단을 오르는 최소 비용은 얼마인가.
#f(n) = min(f(n-2) + cost(n-2), f(n-1) + cost(n-1))

def minCostStair(stair_cost):
    total_count = len(stair_cost)
    arr = [0]*(total_count+1)

    for i in range(2, total_count+1): # 마지막 계단까지 올라와야 하니까 total_count+1
        cost1 = arr[i-1] + stair_cost[i-1]
        cost2 = arr[i-2]+ stair_cost[i-2]
        arr[i]=min(cost1,cost2)
    return arr[total_count]
stair_cost = [1,2,4,6,2,4,6,1]
print(minCostStair(stair_cost))