# 며칠전에 구글링해도 이해를 못했는데 이번엔 이해했다 어렵다 ㅜ
def solution(numbers):

    answer = [-1] * len(numbers)
    stack = []

    for idx, number in enumerate(numbers):

        while stack and numbers[stack[-1]]<number:
            answer[stack.pop()] = number

        stack.append(idx)

    return answer