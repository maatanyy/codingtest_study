# 고민했는데 해결 못한 부분
# 1. 일단 이제 반복문을 통해 max_val 만큼 ㅂ교해야하는데 원래 배열의 정보가 바뀜
# -> 1번 문제를 해결하기 위해 visited 사용!
# DFS에 대해 한 70~80%는 아는 거 같으넫 나머지를 애매하게 알아서 아직 혼자 짜다 보면 조금씩 꼬인다
# 기본적인 부분은 어늦정ㄷ ㅗ이해한거같은데 아오
# 전체적인 접근은 맞ㅇㅆ으나 아직 연습이 부족
import sys
sys.setrecursionlimit(100000)
r = sys.stdin.readline

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, h):

    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]

        if (0 <= nx < N) and (0 <= ny < N) and not visit[nx][ny] and zone[nx][ny] > h:
            visit[nx][ny] = True
            dfs(nx, ny, h)


N = int(r())
zone = [list(map(int, r().split())) for _ in range(N)]

ans = 1
for k in range(max(map(max, zone))):
    visit = [[False]*N for _ in range(N)]
    safe = 0
    for i in range(N):
        for j in range(N):
            if zone[i][j] > k and not visit[i][j]:
                safe += 1
                visit[i][j] = True
                dfs(i, j, k)
    ans = max(ans, safe)

print(ans)