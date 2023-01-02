#page 311
# 어떻게하면 그룹을 최소화 할 수 있나가 핵심이었는데
# 그룹수가 최소인 것 부터 묶는 방식으로 접근하였다  < 여기까진 해결
# 그 다음으로, data의 원소에 접근하여 count로 세는 방식을 사용!  < 이 부분을 좀 더 연습해야할 것 같다!
n = input()
data = list(map(int, input().split()))

group = 0
count =0
data.sort()

for i in data:
    count+=1
    if count >= i:
        count=0
        group+=1
print(group)
