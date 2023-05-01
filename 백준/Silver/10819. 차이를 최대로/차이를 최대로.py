from itertools import permutations

num = int(input())

value = list(map(int, input().split()))

example = list(permutations(value,num))

sum = 0

for i in example:
    temp = len(i)
    sum2 = 0
    for j in range(1, temp):
        sum2+=abs(i[j]-i[j-1])

    sum = max(sum, sum2)

print(sum)

