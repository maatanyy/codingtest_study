import numpy as np
def solution(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)

    ans = np.dot(arr1,arr2)
    answer = ans.tolist()

    return answer