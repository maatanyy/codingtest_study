import math

def lcm(a, b):
    return int(a * b/math.gcd(a, b))

def solution(arr):
    answer = 0

    list = []
    for i in range(len(arr)):
        if len(list)==0:
            list.append(arr[i])
        else:
            list.append(lcm(list.pop(),arr[i]))

    answer = list[-1]

    return answer