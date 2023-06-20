# 책 보고 하나씩 이해함.. 꾸준히 복습해서 익숙해질 필요
# 잘한점 바향 바꾸는 함수는 완벽히 이해함
# 그리고 이제 가본곳을 구별하기 위해 맵의 크기와 똑같은 크기의 0으로 맵 초기화 한다는 걸 배움
# 그리고 4가지다 갈 수 없는 경우를 위해 check 쓰는 것도 배움

n, m = map(int,input().split())

x,y,direction = map(int,input().split())

graph = []

arr = [[0] * (m) for _ in range(n)]
# 갔나 안갔나 체크하는 맵

arr[x][y] = 1

for i in range(m):
    graph.append(list(map(int,input().split())))
# 1이면 바다

def change_diretion():
    global direction
    direction-=1
    if direction==-1:
        direction = 3

# 북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

count = 1
check_point = 0

while True:
    change_diretion()

    nx = x+dx[direction]
    ny = y+dy[direction]

    if graph[nx][ny]==0 and arr[nx][ny]==0:
        arr[nx][ny]=1
        x = nx
        y = ny
        check_point = 0
        count+=1
        continue

    else:
        check_point+=1

    if check_point ==4:
        nx = x-dx[direction]
        ny = y-dy[direction]

        if graph[nx][ny]==0:
            x = nx
            y = ny
        else:
            break

        check_point = 0

print(count)

















