def solution(num_list):
    multy = 1
    for i in num_list:
        multy = multy * i
    plus = sum(num_list)
    plus = plus*plus
    return 1 if plus > multy else 0