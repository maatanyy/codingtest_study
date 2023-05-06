# 처음에 했는데 시간 초과로 못 풀었다가
# 찾아보다 투포인터를 알게 되었는데 이해 못해서 어려웠다
# partial_sum -=sequence[left] 이 부분이 너무 이해가 어려웠다
# 다시 봐야할듯
def solution(sequence, k):
    partial_sum = 0
    right = 0
    result = []
    for left in range(len(sequence)):

        while right<len(sequence) and partial_sum <k:
            partial_sum+=sequence[right]
            right+=1

        if partial_sum == k:
            if not result:
                result = [left,right-1]
            else:
                result = [left,right-1] if result[1] - result[0] > right-1-left else result

        partial_sum -=sequence[left]

    return result



