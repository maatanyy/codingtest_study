def solution(arr1, arr2):

    answer = []
    for i in range(len(arr1)):
        arr = []
        for j in range(len(arr2[0])):
            sum = 0
            for k in range(len(arr1[0])):
                sum+=arr1[i][k]*arr2[k][j]
            arr.append(sum)
        answer.append(arr)
    return answer

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

print(solution(arr1,arr2))