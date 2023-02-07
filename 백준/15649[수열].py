from itertools import permutations
x, y = map(int,input().split())
li = []

for i in range(x):
    li.append(i+1)

data = list(permutations(li, y))

for i in data:
    a = len(i)
    for j in range(a):
        print(i[j], end=' ')
    print('')