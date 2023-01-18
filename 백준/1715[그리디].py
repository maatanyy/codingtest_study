# 두 가지를 배움 1 heapq 생각보다 쓰기 쉬워서 앞으로 유용하게 쓸듯  더한 값을 다시 넣어주는게 매우 인상 깊고 유용하게 쓰일 것 같다는 생각이 듬
# 만약 수가 하나만 있을 경우 비교횟수가 0임 나는 그 수 자체라고 생각해서 오지게 헤맸는데 걍 비교횟수가0이었다
# heapq 를 잘 기억해두자!!!!!!!! 특히 힙큐 푸시할 때
## arr =[] 만들어 두고 heapq.happush(arr,~~~int~~) 좋았따
import sys
import heapq

x = int(input())
arr=[]

for _ in range(x):
    heapq.heappush(arr, int(sys.stdin.readline()))

if len(arr) == 1:
    print(0)

else:
    answer = 0
    while len(arr) > 1:
        tempval1 = heapq.heappop(arr)
        tempval2 = heapq.heappop(arr)
        answer += tempval1 + tempval2
        heapq.heappush(arr, tempval1 + tempval2)

    print(answer)