# 잘 풀었는데 실패해서 질문게시판을 읽다보니
# 내 코드로 하면 이제 1,2면 1에서 2로 단방향으로 추가되는걸 확인할 수 있었다
# 이건 내가 처음이라 그런 거 같고 다음부터는 맞출 수 있을 것 같다
# array[].append()로 넣어주는 아이디어 좋았던 것 같다
num = int(input())
pair = int(input())
array = [[] for _ in range(num+1)]
count = 0
visited = [False] * (num+1)

for _ in range(pair):
    x, y = map(int, input().split())

    array[x].append(y)
    array[y].append(x)

def dfs(array, v, visited):
    visited[v] = True

    for i in array[v]:
        if not visited[i]:
            dfs(array, i, visited)

dfs(array, 1, visited)

for i in visited:
    if i == True:
        count+=1

print(count-1)  #처음 시작점 빼기

