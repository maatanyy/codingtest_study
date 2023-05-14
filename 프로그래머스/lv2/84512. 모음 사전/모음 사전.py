from itertools import product
def solution(word):
    dictionary =[]
    temp = ['A','E','I','O','U']
    for i in range(5):
        dictionary += list(product(temp,repeat=i+1))
    dictionary.sort()

    dictionary2 = []

    for i in dictionary:
        sum=''
        for j in i:
            sum+=j
        dictionary2.append(sum)


    answer = dictionary2.index(word)
    return answer+1

