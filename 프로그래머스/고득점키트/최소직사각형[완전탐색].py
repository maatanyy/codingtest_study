def solution(sizes):
    temp = []
    temp2 = []
    for i in range(len(sizes)):
        temp.append(max(sizes[i]))
        temp2.append(min(sizes[i]))

    answer = max(temp) * max(temp2)
    return answer