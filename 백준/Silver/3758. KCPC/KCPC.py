# 첫 시도 실패
# 구조체를 생각했는데, 클래스를 정의하거나, 딕셔너리를 통해 해결가능한듯
# 딕셔너리를 통한 해결방법이 참신해서 찾아서 참고하여 풀었음
# https://hueco.tistory.com/m/291 참고
import sys

for _ in range(int(input())):
    teamnum, question, teamid, logentry = map(int,sys.stdin.readline().split())

    # 사람수만큼 점수총합, 제출횟수, 제출시간
    record = {x:[0,0,0] for x in range(1, teamnum+1)}

    # 문제의 개수만큼 0으로 초기화해서 score 딕셔너리 만듬
    score = {x:[0] * (question+1) for x in range(1, teamnum+1)}


    #로그만큼 넣어주는 계산, score 비교를 통해 큰 값만 넣어줌(이부분을 해결못했었음)
    for time in range(1, logentry+1):
        a, b, c = map(int,sys.stdin.readline().split())

        if score[a][b] < c:
            score[a][b] = c
            record[a][0] = sum(score[a])

        record[a][1]+=1
        record[a][2] = time

    #print(record)
    # 이걸 왜 다시 list로 감싸나 했는데 마지막에 teamid로 찾을 때 편하다.
    results = list(record.items())
    #print(results)

    results.sort(key=lambda x:(-x[1][0],x[1][1],x[1][2]))

    for i in range(len(results)):
        if results[i][0] == teamid:
            print(i+1)

