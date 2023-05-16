from itertools import combinations
import math

def solution(nums):
    answer = 0
    values = list(combinations(nums,3))

    for i in values:
        sum = 0
        for j in i:
            sum+=j

        if is_prime(sum) == False:
            answer+=1

    return answer

nums = [1,2,7,6,4]

def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i==0:
            return True
    return False

print(solution(nums))