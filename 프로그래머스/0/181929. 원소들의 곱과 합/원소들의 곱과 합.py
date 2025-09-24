def solution(num_list):
    answer = 0
    x = 1
    y = 0
    for i in range(len(num_list)):
        x = x * num_list[i]
        y = y + num_list[i]
        i+=1
    if x < y**2:
        answer = 1
    elif x > y**2:
        answer = 0
    return answer