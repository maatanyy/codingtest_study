def solution(k, m, score):
    score.sort(reverse= True)

    #print(score)
    answer = 0
    
    for i in range(len(score) // m):
        answer += score[i * m + m - 1] * m
        
    return answer
