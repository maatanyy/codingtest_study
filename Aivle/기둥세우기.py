# 기둥 세우기
# 오래된 궁전이 세월의 무게를 이기지 못하고 무너지려고 합니다.
# 관리당국에서는 궁전 곳곳에 기둥을 세우는 보수 공사를 하려고 합니다.
# 직사각형 형태의 궁전을 형성하는 모든 가로, 세로 줄에 대해서 적어도 기둥이 하나씩은 존재하도록 만들고자 할 때 세워야 하는 기둥의 최솟값을 출력하세요.

# 테스트케이스
# 3 3
# 1 1 1
# 1 1 1
# 1 1 1
# ans = 3

# 테스트케이스
# 4 3
# 0 1 1
# 1 0 0
# 0 1 0
# 1 0 1
# ans = 0

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

val1 = 0
val2 = 0

for t in range(n):
    count = 0
    for k in range(m):
        if graph[t][k] == 0:
            count+=1

    if count == 0:
        val1 += 1

for t in range(m):
    count = 0
    for k in range(n):
        if graph[k][t] == 0:
            count += 1

    if count == 0:
        val2 += 1


print(max(val1, val2))