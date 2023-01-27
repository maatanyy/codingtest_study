def solution(score):
    answer = []
    temp = []
    for i in range(len(score)):
        temp.append((score[i][1] + score[i][0])/2)

    arr = sorted(temp,reverse=True)

    for i in range(len(score)):
        answer.append(arr.index(temp[i]))

    for i in range(len(score)):
        answer[i] = answer[i]+1
    return answer

print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))