# 에이블 분리수거장
#
# 두정동에는 N개의 아파트 단지가 일직선상에 존재합니다. 각 아파트 단지에는 1번부터 N번까지 번호가 붙어있습니다.
# 두정동 동사무소에서는 아파트 단지 중 한 곳에 분리수거장을 지으려고 합니다. 분리수거장으로부터 각 주민들까지의 거리의 합이 최소가 되도록 하려면 어떤 아파트 단지에 분리수거장을 지어야 하는지 구하세요.
# 분리수거장으로부터 어떤 주민까지의 거리는 분리수거장이 있는 아파트 단지의 위치와 해당 주민이 거주하는 아파트 단지의 위치의 차로 계산됩니다.
# 단, 조건을 만족하는 아파트 단지가 여러개일 경우, 더 작은 번호의 아파트 단지에 분리수거장을 짓습니다.
#
# 테스트 케이스
# 7
# 475 170
# 28 95
# 506 8361
# 51 3988
# 2 977
# 607 793
# 49 847
# ans = 3
#
# 테스트 케이스
# 11
# 998 2607
# 9422 3358
# 806 80622
# 2848 4153
# 398 180
# 867 22219
# 6514 806
# 246 9462
# 906 43046
# 2592 289
# 8 8486
# ans = 3


num = int(input())

graph = []
temp = []

for _ in range(num):
    a,b = map(int,input().split())
    graph.append([a,b])


for i in range(num):
    sum = 0
    for j in range(num):
        sum += abs(graph[i][0]-graph[j][0])* graph[j][1]

    temp.append(sum)

min_index = temp.index(min(temp))

print(min_index+1)