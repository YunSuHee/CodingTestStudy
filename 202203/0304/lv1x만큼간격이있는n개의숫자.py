def solution(x, n):
    answer = []

    for i in range (n):
        a=x+i*x
        answer.append(a)
    return answer

# def number_generator(x, n):

#     return [i * x + x for i in range(n)]
