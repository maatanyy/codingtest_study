from itertools import permutations

def solution(ability):
    answer = 0
    result = list(permutations(ability, len(ability[0])))
    
    for i in range(len(result)):
        total = 0
        
        for k in range(len(result[0])):
            total += result[i][k][k]
        answer = max(answer,total)
            
    return answer