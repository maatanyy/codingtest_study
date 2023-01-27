def solution(participant, completion):
    answer = ''

    dic = {}

    for i in participant:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    for i in completion:
        if i in dic:
            dic[i] -= 1

    for i in dic:
        if dic[i] != 0:
            answer += i
    return answer