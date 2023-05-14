import sys
import heapq

INF = int(1e9)

testcase = int(input())

for _ in range(testcase):

    # n 교차로, m 도로, t 목적지 후보의 개수
    n, m, t = map(int,sys.stdin.readline().split())


    # 목적지 후보 보관
    templist = []
    answer = []

    graph = [[] * (n+1) for _ in range(n+1)]

    # s 예술가 출발위치, g와 h는 교차로
    s, g, h = map(int, sys.stdin.readline().split())

    for _ in range(m):
        a, b, c = map(int,sys.stdin.readline().split())
        graph[a].append((b,c))   # a에서 b까지 c
        graph[b].append((a,c))

    #교차로 담음
    for _ in range(t):
        x = int(input())
        templist.append(x)

    def dij(start):
        q = []
        distance = [INF] * (n + 1)
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for i in graph[now]:
                cost = dist + i[1]

                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

        return distance

    temp0 = dij(s)
    temp1 = dij(g)
    temp2 = dij(h)

    for val in templist:
        if temp0[g] + temp1[h]+ temp2[val] == temp0[val] or temp0[h] +temp2[g] + temp1[val] == temp0[val]:
            answer.append(val)

    answer.sort()
    for i in answer:
        print(i,end=' ')





