# 에이블 오리농법
# 농부 민겸은 밭에서 농사를 짓습니다.
# 민겸의 밭은 N × N 크기의 정사각형 모양입니다.
# 즉, N^2개의 1 × 1 크기의 땅으로 나눌 수 있습니다.
# 각 땅은 빈 땅, 작물만 있는 땅, 잡초만 있는 땅으로 구분됩니다. 민겸은 잡초를 손쉽게 제거하기 위해 최첨단 오리 농법을 도입했습니다.
# 오리 인덕은 식탐이 많기 때문에 민겸이 정한 어떤 가로줄 또는 세로줄의 잡초와 작물을 모두 먹습니다.
# 인덕이 먹을 수 있는 양에 한계는 없고, 민겸은 인덕을 원하는 만큼 이용할 수 있습니다.
# 똑똑한 민겸은 인덕을 적절히 이용하여 모든 작물을 보존하면서 최대한 많은 잡초를 없앴습니다.
# 이때 잡초만 있는 땅이 몇 개 남아있는지 알아봅시다.


###################
# 테스트케이스
# 4
# 1 0 1 0
# 0 2 0 2
# 2 0 0 0
# 2 1 2 2
# ans = 2

# 4
# 0 0 1 2
# 1 2 0 2
# 0 0 0 1
# 2 1 0 0
# ans = 4

num = int(input())

graph = []

for _ in range(num):
    graph.append(list(map(int,input().split())))



for i in range(num):
    count = 0
    for j in range(num):
        if graph[i][j] == 0 or graph[i][j]==2:
            count+=1

    if count==num:
        for j in range(num):
            graph[i][j] = 0


for i in range(num):
    count = 0
    for j in range(num):
        if graph[j][i] == 0 or graph[j][i] == 2:
            count += 1

    if count == num:
        for j in range(num):
            graph[j][i] = 0

ans = 0

for i in range(num):
    for j in range(num):
        if graph[i][j]==2:
            ans+=1

print(ans)
