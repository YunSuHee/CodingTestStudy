#recursive DP

#탑다운 방식(재귀) -> 스택이 리밋이 있기 떄문에 값이 크면 오류가 생겨
fib_array = [0,1]

def fib_recur_dp(n):
    if n < len(fib_array):
        return fib_array[n]
    else:
        fib = fib_recur_dp(n-1)+ fib_recur_dp(n-2)
        fib_array.append(fib)
        return fib

#보텀업(반복)

def fib_dp(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    fib_array=[0,1]

    for i in range(2,n):
        num = fib_array[i-1]+ fib_array[i-2]
        fib_array.append(num)
    return fib_array[n]