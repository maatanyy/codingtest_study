from collections import deque
n = int(input())
ans = []

for _ in range(n):

    length = int(input())
    graph = [[0]*(length) for _ in range(length)]

    x, y = map(int, input().split())
    finx, finy = map(int, input().split())
    visited = [[False]*(length) for _ in range(length)]

    dx = [ 2, 2, 1, 1, -2, -2, -1, -1 ]
    dy = [ 1,-1, 2,-2, 1, -1, 2, -2 ]

    def bfs(x,y):
        q = deque()
        count = 0
        q.append((x,y,count))
        visited[x][y] = 1

        while q:
            x, y, count = q.popleft()

            if x==finx and y==finy:
                ans.append(count)
                break

            for i in range(8):
                nx = x+dx[i]
                ny = y+dy[i]

                if 0<=nx<length and 0<=ny<length and visited[nx][ny]==False:
                    visited[nx][ny] = True
                    q.append((nx, ny, count+1))


    bfs(x,y)

for i in ans:
    print(i)














