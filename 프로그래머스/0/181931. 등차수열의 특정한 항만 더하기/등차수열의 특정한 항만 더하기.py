# 등차수열 n번째 항은 a+(n−1)da+(n−1)d 이지만 반복문 인덱스가 0부터 시작하므로 a+n×da+n×d 로 계산.
def solution(a, d, included):
    answer = 0
    for n in range(len(included)):
        y = a + n * d
        if included[n]:
            answer += y
    return answer