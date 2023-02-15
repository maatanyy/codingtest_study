# 3, 30일 때 3이 앞에 오게 하는 법을 아무리 고민해도 몰랐는데 X*3으로 하는 걸 보고 매우 놀랐다
# 이런 생각을 어떻게 하는건지 신기할 따름이다
# 그리고 0000의 경우 0으로 출력이 나와야해서 int로 바꿨다가 다시 str로 바꿔서 출력하는 트릭도 참
# 이런 생각을 어떻게 하는지 신기할 따름
def solution(numbers):
    answer = ''
    temp = [str(x) for x in numbers]
    #print(temp)
    hello = sorted(temp, key=lambda x:x*3, reverse=True)
    answer = ''.join(hello)
    answer = str(int(answer))
    return answer

numbers = [0,0,0,0]


print(solution(numbers))