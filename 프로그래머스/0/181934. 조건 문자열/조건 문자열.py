def solution(ineq, eq, n, m):
    answer = 0
    if ineq == ">":
        if eq == "!":
            answer = n > m
        else: # eq == "="
            answer = n >= m
    else: # ineq == "<":
        if eq == "!":
            answer = n < m
        else:  # eq == "="
            answer = n <= m
    return int(answer)