def solution(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        if code[i] == "1" and mode == 0:
            mode = 1
        elif code[i] == "1" and mode == 1:
            mode = 0

        if mode == 0:
            if code[i] != "1" and i%2==0:
                answer += code[i]
        else:
            if code[i] != "1" and i%2==1:
                answer += code[i]
    return answer if answer else "EMPTY"