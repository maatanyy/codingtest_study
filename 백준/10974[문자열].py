from itertools import permutations
num = int(input())
arr = []
for i in range(num):
    arr.append(i+1)

ans = list(permutations(arr,num))

for i in ans:
    for j in i:
        print(j,end=' ')
    print('')
