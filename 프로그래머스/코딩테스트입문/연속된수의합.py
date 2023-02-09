def solution(num, total):
    answer = []
    sum = 0
    for i in range(1, num):
        sum += i
    x = (total - sum) // num

    for i in range(num):
        answer.append(x + i)
    return answer