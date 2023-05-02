from math import sqrt
from itertools import permutations

def is_print(number):

    temp = int(sqrt(number))

    if number==0:
        return True

    elif number==1:
        return True

    elif number==2:
        return False

    elif number==3:
        return False
    else:
        for i in range(2,temp+1):
            if number%i==0:
                return True

    return False


def solution(numbers):
    answer = 0
    values = []
    temp = []
    for i in numbers:
        values.append(i)

    for i in range(len(numbers)):
        temp2 = list(permutations(values,i+1))
        temp +=temp2

    sum = []

    for i in temp:
        t=''
        for j in range(len(i)):
            t+= i[j]
        sum.append(int(t))

    sum = set(sum)

    for i in sum:
        if is_print(i)==False:
            answer+=1

    return answer