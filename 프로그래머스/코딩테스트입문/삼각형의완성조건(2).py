def solution(sides):
    temp = max(sides)
    temp2 = min(sides)
    temp3 = temp + temp2 - 1
    count = 0
    for i in range(1, temp):
        if i + temp2 > temp:
            count += 1

    count += temp3 - temp + 1
    answer = count
    return answer