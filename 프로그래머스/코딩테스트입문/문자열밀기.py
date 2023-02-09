import sys
def solution(A, B):
    count=0
    length = len(A)
    if A == B:
        answer =0
        return answer
    for i in range(length):
        count+=1
        A = A[-1]+A[:-1]
        if A == B:
            return count
        else:
            answer=-1
    return answer