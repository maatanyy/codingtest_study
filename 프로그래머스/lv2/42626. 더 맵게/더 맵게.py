import heapq
def solution(scoville, K):
    answer = 0
    q = []
    
    for i in scoville:
        heapq.heappush(q,i)
        
    while True:
            
        a = heapq.heappop(q)
        
        if a>=K:
            break
        else:
            if len(q)==0:
                return -1
            b = heapq.heappop(q)
            answer+=1
            heapq.heappush(q,a+2*b)
        
    return answer