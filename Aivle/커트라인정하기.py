# 커트라인정하기
# 민겸은 학생들을 가르치는 교사입니다.
# 민겸은 N명의 학생들을 일렬로 세워 쪽지 시험을 보게 했습니다.
# 쪽지 시험에서 P점 이상을 받은 학생들은 시험에 합격합니다.
# 또한 P점 미만의 학생들 중에서도 좌우로 인접한 P점 이상의 점수를 받은 학생이 한 명 이상이면 그 학생도 합격시키려고 합니다.
# 민겸이 합격시키고자 하는 학생의 수의 최댓값은 K입니다. K명 이하의 학생이 합격하도록 하면서
# 가능한 한 많은 학생들이 시험에 합격할 수 있는 P의 최댓값을 구하세요.
# 이때, 시험에 합격하는 학생이 없을 수도 있습니다.
# 테스트 케이스
# 입력
# 5 3
# 50 30 40 50 70
#
# 출력
# 70
#
# 입력
# 5 4
#
# 출력
# 80 60 100 75 70

num, k = map(int, input().split())

temp = list(map(int, input().split()))
ans = []
score = -1

for i in range(num):
    count = 0
    score = temp[i]

    for j in range(num):

        if (j==0 and temp[j]>=score) or (j==0 and temp[j+1]>= score):
            count+=1

        elif (j== num-1 and temp[j]>= score) or (j==num-1 and temp[j-1]>=score):
            count+=1

        elif 1<=j<num-1 and ((temp[j]>=score) or (temp[j-1] >=score or temp[j+1]>=score)):
            count+=1

    if count<=k:
        ans.append([score, count])

if len(ans)==0:
    print(min(temp)-1)

else:
    ans.sort(key= lambda x:(-x[1],-x[0]))
    print(ans[0][0])


