from itertools import permutations
def solution(k, dungeons):
    answer = 0
    temp = list(permutations(dungeons,len(dungeons)))
    
    
    for i in temp:
        start = k
        count = 0
        for t in i:
            if start >= t[0] and start>=t[1]:
                start-=t[1]
                count+=1
            else:
                break
        
        answer = max(answer,count)
                
    return answer