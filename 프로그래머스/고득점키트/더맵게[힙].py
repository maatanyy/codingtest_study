# heapq를 보기만 해고 생각하며 쓴 건 처음인데 매우 유용했다
# 익숙해지면 더 좋을 듯!
import heapq

def solution(scoville, K):
    heap = []
    for i in range(len(scoville)):
        heapq.heappush(heap, scoville[i])

    answer = 0
    while True:
        if heap[0]>=K:
            break

        elif len(heap)==2 and heap[0]+(heap[1]*2)<K:
            answer=-1
            break
        else:
            result = heapq.heappop(heap)
            result2 = heapq.heappop(heap)
            temp = result+result2*2
            heapq.heappush(heap,temp)
            answer+=1
    return answer


scoville = [1, 2, 3, 9, 10, 12]
solution(scoville, 7)