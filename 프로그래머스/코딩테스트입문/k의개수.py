#처음에는 단순히 처음과 끝 값 증가하며 확인하려고 함
# 하지만 이럴 경우 11, 1일경우 하나만 count하는 에러 발생
# 해결하기 위해 반복문 2개 씀
def solution(i, j, k):
    answer = 0
    for x in range(i, j + 1):
        for y in str(x):
            if str(k) in y:
                answer += 1

    return answer