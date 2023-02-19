# 스스로 해결하여 뿌듯하나 다른 사람 풀이를 보니 한줄컷 한 사람도 있군
# 갈 길이 상당히 멀다
from itertools import permutations
def solution(k, dungeons):
    v1 = k
    temp = list(permutations(dungeons, len(dungeons)))

    answer = -1
    for val in temp:
        k=v1
        tempAnswer = 0
        for j in val:
            if k-j[0]>=0 and k-j[1]>=0:
                k = k-j[1]
                tempAnswer+=1

        if tempAnswer >=answer:
            answer=tempAnswer

    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))