## 많은 걸 배운 문제다
# 아주 알찼다.
# 플로이드 워셜도 써보고 디엑스트라도 써보고 혼자 잘 해결했다
# 하지만 2가지 문제점이 있어서 검색을 했는데
# 첫번째, 기존 내 코드는 다익스트라 함수에서 return을 주지 않아서 이렇게 여러번 호출할 경우 대비를 할 수 없었는데
# 단순히 dis 배열을 안에 넣어주고 리턴하는 걸로 접근 할 수 있다는 것을 배웠고
# 두 번째로 예외의 경우 즉 갈 수 없어서 -1이 나와야 할 경우 자꾸 에러가 나왔는데
# 값이 INF보다 같거나 크게해서 예외처리 한다고 배웠다
# 기존 내 코드 같은 경우 ans ==INF 일 경우 예외였는데
# 여기서는 INF가 여러번 더해질 경우 INF를 초과하는데 이걸 생각 못했었는데 여기서 배웠다
# 앞으로 >=INF로 하면 될 것 같다는 생각이 들었다
# 최근에 푼 문제들 중에 가장 많이 배운 것 같다
import heapq
import sys
import math

INF = int(1e9)

n, m = map(int, sys.stdin.readline().split())

graph = [ []*(n+1) for _ in range(n+1)]


for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


def dij(start):
    distance = [INF] * (n + 1)
    distance[start] = 0

    q =[]
    heapq.heappush(q, (0,start))

    while q:
        dis, nod = heapq.heappop(q)

        if distance[nod] < dis:
            continue

        for i in graph[nod]:
            cost = dis + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

    return distance

x, y = map(int,input().split())

temp1 = dij(1)
temp2 = dij(x)
temp3 = dij(y)

ans1 = temp1[x] + temp2[y] + temp3[n]
ans2 = temp1[y] + temp3[x] + temp2[n]

answer = min(ans1, ans2)
if answer >= INF:
    answer = -1
print(answer)