from itertools import permutations
def solution(k, dungeons):
    piro = k
    answer = 0
    temp = list(permutations(dungeons, len(dungeons)))

    for i in temp:
        energy = piro
        tempanswer = 0
        for j in i:
            if energy >= j[0] and energy>=j[1]:
                tempanswer+=1
                energy = energy-j[1]
        answer = max(answer,tempanswer)

    return answer