import sys

# 방 없으면 -10 ~ +10으로 하나 파고 입장
# 입장 가능한 방이 있으면 들가고 대기
# 방이 여러개면 먼저 생긴방에
# 방의 정원이 모두 차면 게임 시작

# 플레이어의 수 p, 플레이어의 닉네임 n, 플레이어의 레벨 l, 방 한개의 정원 m이 주어졌을 때
# 위와 같은 방법으로 매칭해주고 최종적으로 만들어진 방의 상태와 입장 플레이어들을 출력하는 프로그램을 작성하자.

p, m = map(int,input().split())

room = []


for _ in range(p):
    level, nickname = input().split()
    level = int(level)
    count = 0
    Flag = False

    if len(room)==0:
        temp = [level,[[level, nickname]]]
        room.append(temp)

    else:
        for miniroom in room:

            if miniroom[0]-10 <= level and level <= miniroom[0]+10 and len(miniroom[1])<m:
                temp = [level, nickname]
                miniroom[1].append(temp)
                count = 1
                Flag = True
                break

            elif miniroom[0]-10 <= level and level <=miniroom[0]+10 and len(miniroom[1])==m: # 만약 같고 다른 남는 방 있으면 안 만들고 넣으면 됨
                continue
                temp = [level, [[level,nickname]]]
                room.append(temp)
                count = 2
                break

        if count == 0 or Flag==False:
            temp = [level, [[level,nickname]]]
            room.append(temp)

for i in room:
    i[1].sort(key=lambda x:x[1])


for i in room:
    if len(i[1])==m:
        print('Started!')
        for j in i[1]:
            print(j[0], j[1])

    elif len(i[1]) != m:

        print('Waiting!')

        for j in i[1]:
            print(j[0], j[1])




