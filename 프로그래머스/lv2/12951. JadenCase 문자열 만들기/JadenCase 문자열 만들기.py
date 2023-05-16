def solution(s):
    answer = []

    s = s.split(' ')

    for word in s:
        word = word.capitalize()
        answer.append(word)

    answer = " ".join(answer)

    return answer