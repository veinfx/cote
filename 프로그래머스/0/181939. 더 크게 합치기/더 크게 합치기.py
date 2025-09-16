def solution(a, b):
    return int(str(b) + str(a) if str(b) + str(a) > str(a)+  str(b) else  str(a)+  str(b))