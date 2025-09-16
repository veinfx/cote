def solution(number, n, m):
    if int(not(number%n) and not(number%m)):
        answer = 1
    else:
        answer = 0
    return answer