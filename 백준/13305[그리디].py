# 하 시파,,, test case 다 돌아가고 질문게시판에 있는 반례들도 다 돌아가는데 이유를 모르겠어서 다른 사람 풀이 봤다
# 방법은 나랑 똑같은데 내 코드가 너무 지저분해서 어디서 형 변환하다 꼬였나 싶다
# 아이디어는 똑같았다 다만 수가 커서 import sys 이용해서 입력을 받았었다

n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

value = oil[0] * road[0]
now_oil = oil[0]

for i in range(1, len(road)):
    if now_oil <= oil[i]:
        value += now_oil * road[i]
    elif now_oil > oil[i]:
        value += oil[i] * road[i]
        now_oil = oil[i]

print(value)

