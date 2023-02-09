def solution(numlist, n):
    answer = []
    numlist.sort(reverse=True)
    numlist.sort(key=lambda x: abs(n - x))

    return numlist

