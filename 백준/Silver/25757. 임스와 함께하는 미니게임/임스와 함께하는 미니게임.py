import sys

#윷놀이 y 2
#같은 그림 찾기 f 3
#원카드 o 4

#플레이 시작 횟수 n
# 게임의 종류가 주어질 때 최대 몇 번 할 수 있는지
# 동명이인 x 한 사람이랑 다시 x

a, b = input().split()

a = int(a)

if b=='Y':
    max = 2
elif b=='F':
    max = 3
elif b =='O':
    max = 4

count = 0

values = []
for _ in range(a):
    name = input()
    values.append(name)

values = set(values)
temp = len(values)

ans = temp//(max-1)
print(ans)






















