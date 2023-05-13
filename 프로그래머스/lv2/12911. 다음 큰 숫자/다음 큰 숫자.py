def solution(n):
    answer = 0
    val = ''
    temp = bin(n)
    temp = temp[2:]

    val = temp.count('1')

    while True:
        n = n+1
        tempval = bin(n)
        countOne = tempval.count('1')

        if countOne == val:
            answer = n
            break

    return answer


