# 선물을 무작위로 나눠주면 아이들 사이에 다툼이 발생합니다.
# 모든 종류의 선물에 대해 개수를 공평하게 나눠줘야 합니다.
# 예를 들어 3명의 아이들에게 선물을 나눠준다고 가정하겠습니다.
# 이 경우 아이 1명 당 1번 종류의 선물 a_1 / 3개, 2번 종류의 선물 a_2 / 3개, …, N번 종류의 선물 a_N / 3개를 받습니다.
# 철수는 선물을 남기지 않고 최대한 많은 아이들에게 나눠주려고 합니다.
# 선물을 받게 되는 아이들의 최대 명수를 구하는 프로그램을 작성해주세요.
num = int(input())

temp = list(map(int,input().split()))

temp.sort()

check = max(temp)

length = len(temp)

start = 1

for i in range(1, check):
    cou = 0
    for j in range(length):

        if temp[j] % i==0:
            cou+=1

    if cou == length:
        start = i

print(start)
