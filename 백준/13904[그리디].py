# 정렬까지는 매우 잘했음
# 문제는 이걸 어케 비교해서 넣어줘야 하는건데 아무리 생각해도 아이디어가 안떠오름
# 인터넷 찾아보고 해결했다
# visited 를 dfs에서도 그렇고 아직 잘 못쓰는데 이 개념을 머리에 잘 넣어둬야할 것 같음
# https://hello70825.tistory.com/295 참고
num = int(input())
arr = []

for i in range(num):
    x, y = map(int,input().split())
    arr.append([x,y])

arr.sort(key=lambda x : -x[1])
ans = 0
visited = [0] * 1001

print(arr)
for day, val in arr:
    for i in range(day,0,-1):
        if not visited[i]:
            visited[i]=1
            ans+=val
            break

print(ans)



