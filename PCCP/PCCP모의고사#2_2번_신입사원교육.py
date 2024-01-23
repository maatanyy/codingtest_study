import heapq

def solution(ability, number):
    answer = 0
    
    q = []
    
    for i in ability:
        heapq.heappush(q,i)
        
    for _ in range(number):
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        c = a+b
        heapq.heappush(q,c)
        heapq.heappush(q,c)
    
    answer = sum(q)
    return answer