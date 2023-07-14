from itertools import combinations
temp = list(input())

answer = []

temps = []
for i in range(1,len(temp)-1):
    for j in range(i+1,len(temp)):
        temp1 = temp[:i]
        temp2 = temp[i:j]
        temp3 = temp[j:]

        temp1.reverse()
        temp2.reverse()
        temp3.reverse()
        temps.append(temp1+temp2+temp3)

temps.sort()
for i in temps[0]:
    print(i,end='')

