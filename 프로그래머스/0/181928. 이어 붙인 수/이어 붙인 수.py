def solution(num_list):
    str_a = ""
    str_b = ""
    for i in num_list:
        if i%2 ==0:
            str_a = str_a + str(i)
        else:
            str_b = str_b + str(i)
    # print("짝", str_a, "홀", str_b, "합", int(str_a)+ int(str_b))
    answer = int(str_a)+ int(str_b)
    return answer