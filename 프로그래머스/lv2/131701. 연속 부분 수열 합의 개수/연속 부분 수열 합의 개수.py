def solution(elements):
    answer = []

    length = len(elements)

    elements = 2 * elements
    #print(elements)

    for i in range(length):
        for j in range(1, length):
            val = sum(elements[i:i+j])
            answer.append(val)

    answer = set(answer)
    answer = len(answer)

    return answer+1