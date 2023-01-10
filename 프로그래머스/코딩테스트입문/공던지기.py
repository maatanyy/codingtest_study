def solution(numbers, k):
    answer = 0
    index = 1
    for i in range(k-1):
        index += 2
        if index >= len(numbers) :
            index = index-len(numbers)

    answer = index
    return answer