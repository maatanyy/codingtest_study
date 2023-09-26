def solution(participant, completion):
    temp = dict()
    answer = ""

    for i in participant:
        if i not in temp:
            temp[i] = 1
        else:
            temp[i] += 1

    for j in completion:
        if temp[j] == 0:
            answer = j
            return answer
        else:
            temp[j] -= 1

    for k,v in temp.items():
        if v !=0:
            answer = k
            break
    return answer