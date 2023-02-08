# 배열을 3개로 정의하는 것 까지는 접근을 하였으나 i for i~~ 어쩌구 등으로 식으로 할라했는데 규칙이 안보였다
# 그냥 규칙이 나오는 곳까지 배열로 선언하면 되는 거 였는데 시파
# 그리고 마지막에 인덱스 부분을 고를 때 enumerate부분이 되게 인상 깊다 이 부분은 자주 사용할 것 같아서 암기!
answers= [1,2,3,4,5]

def solution(answers):
    peop1 = [1, 2, 3, 4, 5]
    peop2 = [2, 1, 2, 3, 2, 4, 2, 5]
    peop3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = [0, 0, 0]
    sol = []
    for i in range(len(answers)):
        if answers[i] == peop1[i % 5]:
            answer[0] += 1
        if answers[i] == peop2[i % 8]:
            answer[1] += 1
        if answers[i] == peop3[i % 10]:
            answer[2] += 1

    for index, num in enumerate(answer):
        if num == max(answer):
            sol.append(index+1)

    return sol


print(solution(answers))