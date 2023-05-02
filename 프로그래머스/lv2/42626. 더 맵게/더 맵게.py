import heapq


def solution(scoville, K):
    answer = 0
    q = []
    for i in scoville:
        heapq.heappush(q, i)

    while q:

        if len(q) == 2:
            val1 = heapq.heappop(q)
            val2 = heapq.heappop(q)
            
            if val1>=K:
                return answer
            
            elif val1 + 2 * val2 < K:
                return -1

            elif val1 + 2 * val2 >= K:
                return answer+1

        else:
            val1 = heapq.heappop(q)
            val2 = heapq.heappop(q)

            if val1 >= K:
                return answer

            else:
                answer += 1
                val3 = val1 + 2 * val2
                heapq.heappush(q, val3)

    return answer