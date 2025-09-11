def solution(n, k):
    answer = []
    for i in range(n):
        i +=1
        a = k * i
        if 0 < a <= n:
            answer.append(a)
    return answer