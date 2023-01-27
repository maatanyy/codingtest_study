def solution(chicken):
    answer = 0

    while chicken // 10 >= 1:
        answer += chicken // 10
        rest = chicken % 10
        chicken = chicken // 10 + rest

    return answer