# 가영은 강아지를 키우고 있습니다.
# 가영은 강아지를 잃어버릴 것에 대비해서 목줄에 위치 추적기를 만들고 싶습니다.
# 위치 추적기는 강아지가 달리는 방향을 감지하고 그렇게 얼마나 이동했는지 알 수 있습니다.
# 다시 말해서 움직인 방향과 이동한 거리를 가영의 집 서버로 보냅니다.
# 위치 추적기는 북쪽을 1, 동쪽을 2, 남쪽을 3, 서쪽을 4로 저장합니다.
# 그리고 이동한 거리는 임의의 자연수로 저장합니다.
# 가영의 강아지가 좌표평면 상에 있다고 해봅시다.
# 여기서 y축 방향은 북쪽, x축 방향은 동쪽입니다.
# 만약 가영의 강아지가 (0, 0), (0, 5), (3, 5)로 움직였다면
# 위치 추적기는 (2, 5), (1, 3)을 가영의 개인 서버로 보내야 합니다.
# 여기서 가영의 강아지는 좌표축과 평행하게만 이동한다고 가정하겠습니다.
# 가영의 강아지가 움직인 위치가 주어집니다.
# 그에 따른 위치 추적기가 가영의 서버로 보내야 할 데이터를 만들어 주세요.


num = int(input())

temp = []
for _ in range(num):
    a, b = map(int,input().split())
    temp.append([a,b])

cur = temp[0]
ans = []


for i in range(1, len(temp)):

    if cur[0] == temp[i][0]:
        if cur[1] < temp[i][1]:
            ans.append([2,temp[i][1]-cur[1]])
        else:
            ans.append((4,cur[1]-temp[i][1]))

        cur = [cur[0],temp[i][1]]


    elif cur[1] == temp[i][1]:
        if cur[0] < temp[i][0]:
            ans.append([1,temp[i][0]-cur[0]])

        else:
            ans.append([3,cur[0]-temp[i][0]])

        cur = [temp[i][0], cur[1]]

for i in ans:
    print(i[0],i[1])